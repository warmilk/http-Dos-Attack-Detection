# DoS 漏洞复现 + 基于机器学习的 DoS 攻击检测器

## 准备好复现漏洞的环境

客户端（windows 或 Linux 主机任意）

服务端（Linux主机一台。下文使用 Ubuntu）
* #### 步骤一：服务端主机安装 Apache2 

    `sudo apt update`

    `sudo apt install apache2`

    `apache2 -version`


* #### 步骤二：服务端主机需自定义 Apache 日志文件存放路径

    需要自己指定一下 Apache 日志文件的保存路径（修改方法自行百度），当然不改也行，用默认的 apache 日志存放路径即可，主要是不同的Linux发行版会有不同的存放路径，如ubuntu下apache的默认日志存放路径为 `/var/log/apache2/`。
    
    因为这个日志文件是需要 “投喂” 给脚本用于训练模型的，所以请务必记住设置了存在哪个位置。
  
    `./utils/LogHelper.py` 中我指定了自定义日志的存放路径为 `"/var/log/apache2/custom.log"`

* #### 步骤三：服务端主机需修改 Apache 默认的日志文件内容
    我已经改好了，只需知道以下格式代表什么即可

    `"%d-%b-%Y %T::::%a::::%m::::%s::::%B::::%D::::%U::::%r"`

    `%d` 是 date

    `%b` 是 month

    `%Y` 是 Year

    `%T` 是 Time (hour:min:sec in 24hour clock format)

    `%a` 是 client ip address

    `%m` 是 request method

    `%s` 是 status code

    `%B` 是 size of response in bytes

    `%D` 是 time taken to serve the request

    `%U` 是 url path



* #### 步骤四：服务端主机将修改好的 Apache2 配置文件覆盖默认配置文件 ##

    项目源码内的 `./config/apache/apache2.conf` 文件，是已经根据【步骤三】的内容修改好的apache2配置文件，只需要将它移动到ubantu下的默认路径 `/etc/apache2/` 即可，
  
    命令如下：

    `mv ./config/apache/apache2.conf /etc/apache2/`

    `mv ./config/apache/000-default.conf /etc/apache2/sites-available/`

* #### 步骤四：确认服务端主机的 Apache 服务被成功开启 ##
  
    如果在另一台机器的浏览器，输入 Apache 所在宿主机器的ip地址，能成功加载到 apache 默认的欢迎网页，就说明 apache 配置成功，且已被启动。

    默认的 index.html 存放路径可在 `.\config\apache\000-default.conf` 第12行关于 `DocumentRoot /var/www/html` 的配置处找到）

* #### 步骤四：服务端主机安装 python 程序所需依赖包

    运行 `./install.sh` 即可。

    简要介绍下本项目使用到的核心依赖包：

    `luminol`：用于分析时间序列（项目主页：https://github.com/linkedin/luminol）, 使用了 anomaly_detector 异常检测模块，用于数据预处理
  
    `sklearn`：机器学习框架，用到了 DecisionTreeClassifier 决策树分类器，用于将正常流量和dos攻击的流量分离开

## 漏洞原理

正常的http请求是用两个 \r\n 结尾，`./tests/dos.py` 构造了大量只有一个 \r\n 结尾的请求，http服务端会误认为请求还没结束，于是一直保存连接，直到服务端的连接数过多，最终无法处理别的正常请求

漏洞详情：[exploitDB](https://www.exploit-db.com/exploits/17696)   [CVE-2014-5329](https://nvd.nist.gov/vuln/detail/CVE-2014-5329)    [CVE-2011-3192](https://nvd.nist.gov/vuln/detail/CVE-2011-3192)



## 漏洞复现/利用

服务端主机启动 `python ./tests/dos.py 127.0.0.1:80 index.html` 即可，该命令会对 http://127.0.0.1:80 发动 dos 攻击，也就是服务端主机自己攻击自己 =。= 


## 漏洞验证
以下两种方法任意一种，都可用于验证dos攻击是否成功

* 方法一：服务端主机查看是否产生了自定义格式的 apache dos日志文件

* 方法二：客户端通过浏览器访问服务端ip地址，如果 index.html 无法加载，则证明攻击成功








## 漏洞检测

由于机器学习需要耗费大量硬件资源与时间，以下操作建议放在Linux服务器中执行，不建议使用个人电脑

* #### 步骤一：准备训练模型时所需的数据集

    服务端主机通过 `python ./tests/dos.py 127.0.0.1:80 index.html` 启动攻击即可，会产生大体积的 apache 日志文件。模型的准确性极度依赖于数据集质量，所以这一步准备数据集的时候，越接近真实网络环境越好

* #### 步骤二：数据集预处理
  
    详见 `./Dataset.py` ，这一步主要是对 apache 的日志文件提取特征值/降维减噪操作，夹杂着大量常规的正常流量 + 少量dos攻击流量 的.log文件会被处理为体积小精炼的.csv文件
    
    训练集建议命名为 `train.csv` 并保存在 `./data` 下

    测试集建议命名为 `test.csv` 并保存在 `./data` 下
  
* #### 步骤二：训练模型

    `python App.py [-h] train_filepath test_filepath`

    `train_filepath` ：训练集数据所在路径

    `test_filepath`：测试集数据所在路径

    `python App.py ./data/train.csv ./data/test.csv`

* #### 步骤三：将模型部署到生产环境，迭代调整参模型数提升检测准确率



## TODO
当前是直接在裸操作系统上复现，但为了便于后期维护迁移，我们应该将复现的漏洞环境打包放进docker里

当前数据的预处理是直接读取.log文件处理为.csv，可能先抓到Apache流量的.pcap包，再转为转为.json，再预处理转为.csv会更合适？