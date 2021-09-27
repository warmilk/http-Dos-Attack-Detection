### dos攻击原理
正常的http请求是用两个 \r\n 结尾，这里构造了大量只有一个 \r\n 结尾的请求，http服务端会误认为请求还没结束，于是一直保存连接，直到服务端的连接数过多，最终无法处理别的正常请求

漏洞详情：https://www.exploit-db.com/exploits/17696

CVE: 2014-5329

CVE: 2011-3192

### http request header 的 HOST: 是什么？

我们知道一个IP地址可以对应多个域名，比如假设我有这么几个域名 www.qiniu.com，www.taobao.com和www.jd.com 然后在域名提供商那通过A记录或者CNAME记录的方式最终都和我的虚拟机服务器IP 111.111.111.111关联起来，那么我通过任何一个域名去访问最终解析到的都是IP 111.111.111.111。

但是还是没有提到Host的概念，其实可以这样看，我们的那台虚拟机111.111.111.111上面其实是可以放很很多网站的(不然如果只能放一个网站的话就太不合理了，虚拟机那么多资源都浪费了)，

我们可以把www.qiniu.com，www.taobao.com 和 www.jd.com 这些网站都假设那台虚拟机上面，但是这样会有一个问题，我们每次访问这些域名其实都是解析到服务器IP 111.111.111.111，我怎么来区分每次根据域名显示出不同的网站的内容呢，

其实这就要用到请求头中Host的概念了，每个Host可以看做是我在服务器111.111.111.111上面的一个站点，每次我用那些域名访问的时候都是会解析同一个虚拟机没错，但是我通过不同的 Host 可以区分出我是访问这个虚拟机上的哪个站点。


Tomcat 的 Host 配置示例：

`<Host name="www.qiniu.com" appBase="qiniuwebapp">`

`<Host name="www.taobao.com" appBase="taobaowebapp">`

`<Host name="www.jb.com" appBase="jbwebapp">`