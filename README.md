# DoS ©������ + ���ڻ���ѧϰ�� DoS ���������

## ׼���ø���©���Ļ���

�ͻ��ˣ�windows �� Linux �������⣩

����ˣ�Linux����һ̨������ʹ�� Ubuntu��
* #### ����һ�������������װ Apache2 

    `sudo apt update`

    `sudo apt install apache2`

    `apache2 -version`


* #### �������������������Զ��� Apache ��־�ļ����·��

    ��Ҫ�Լ�ָ��һ�� Apache ��־�ļ��ı���·�����޸ķ������аٶȣ�����Ȼ����Ҳ�У���Ĭ�ϵ� apache ��־���·�����ɣ���Ҫ�ǲ�ͬ��Linux���а���в�ͬ�Ĵ��·������ubuntu��apache��Ĭ����־���·��Ϊ `/var/log/apache2/`��
    
    ��Ϊ�����־�ļ�����Ҫ ��Ͷι�� ���ű�����ѵ��ģ�͵ģ���������ؼ�ס�����˴����ĸ�λ�á�
  
    `./utils/LogHelper.py` ����ָ�����Զ�����־�Ĵ��·��Ϊ `"/var/log/apache2/custom.log"`

* #### ��������������������޸� Apache Ĭ�ϵ���־�ļ�����
    ���Ѿ��ĺ��ˣ�ֻ��֪�����¸�ʽ����ʲô����

    `"%d-%b-%Y %T::::%a::::%m::::%s::::%B::::%D::::%U::::%r"`

    `%d` �� date

    `%b` �� month

    `%Y` �� Year

    `%T` �� Time (hour:min:sec in 24hour clock format)

    `%a` �� client ip address

    `%m` �� request method

    `%s` �� status code

    `%B` �� size of response in bytes

    `%D` �� time taken to serve the request

    `%U` �� url path



* #### �����ģ�������������޸ĺõ� Apache2 �����ļ�����Ĭ�������ļ� ##

    ��ĿԴ���ڵ� `./config/apache/apache2.conf` �ļ������Ѿ����ݡ����������������޸ĺõ�apache2�����ļ���ֻ��Ҫ�����ƶ���ubantu�µ�Ĭ��·�� `/etc/apache2/` ���ɣ�
  
    �������£�

    `mv ./config/apache/apache2.conf /etc/apache2/`

    `mv ./config/apache/000-default.conf /etc/apache2/sites-available/`

* #### �����ģ�ȷ�Ϸ���������� Apache ���񱻳ɹ����� ##
  
    �������һ̨����������������� Apache ��������������ip��ַ���ܳɹ����ص� apache Ĭ�ϵĻ�ӭ��ҳ����˵�� apache ���óɹ������ѱ�������

    Ĭ�ϵ� index.html ���·������ `.\config\apache\000-default.conf` ��12�й��� `DocumentRoot /var/www/html` �����ô��ҵ���

* #### �����ģ������������װ python ��������������

    ���� `./install.sh` ���ɡ�

    ��Ҫ�����±���Ŀʹ�õ��ĺ�����������

    `luminol`�����ڷ���ʱ�����У���Ŀ��ҳ��https://github.com/linkedin/luminol��, ʹ���� anomaly_detector �쳣���ģ�飬��������Ԥ����
  
    `sklearn`������ѧϰ��ܣ��õ��� DecisionTreeClassifier �����������������ڽ�����������dos�������������뿪

## ©��ԭ��

������http������������ \r\n ��β��`./tests/dos.py` �����˴���ֻ��һ�� \r\n ��β������http����˻�����Ϊ����û����������һֱ�������ӣ�ֱ������˵����������࣬�����޷���������������

©�����飺[exploitDB](https://www.exploit-db.com/exploits/17696)   [CVE-2014-5329](https://nvd.nist.gov/vuln/detail/CVE-2014-5329)    [CVE-2011-3192](https://nvd.nist.gov/vuln/detail/CVE-2011-3192)



## ©������/����

������������� `python ./tests/dos.py 127.0.0.1:80 index.html` ���ɣ��������� http://127.0.0.1:80 ���� dos ������Ҳ���Ƿ���������Լ������Լ� =��= 


## ©����֤
�������ַ�������һ�֣�����������֤dos�����Ƿ�ɹ�

* ����һ������������鿴�Ƿ�������Զ����ʽ�� apache dos��־�ļ�

* ���������ͻ���ͨ����������ʷ����ip��ַ����� index.html �޷����أ���֤�������ɹ�








## ©�����

���ڻ���ѧϰ��Ҫ�ķѴ���Ӳ����Դ��ʱ�䣬���²����������Linux��������ִ�У�������ʹ�ø��˵���

* #### ����һ��׼��ѵ��ģ��ʱ��������ݼ�

    ���������ͨ�� `python ./tests/dos.py 127.0.0.1:80 index.html` �����������ɣ������������� apache ��־�ļ���ģ�͵�׼ȷ�Լ������������ݼ�������������һ��׼�����ݼ���ʱ��Խ�ӽ���ʵ���绷��Խ��

* #### ����������ݼ�Ԥ����
  
    ��� `./Dataset.py` ����һ����Ҫ�Ƕ� apache ����־�ļ���ȡ����ֵ/��ά��������������Ŵ���������������� + ����dos�������� ��.log�ļ��ᱻ����Ϊ���С������.csv�ļ�
    
    ѵ������������Ϊ `train.csv` �������� `./data` ��

    ���Լ���������Ϊ `test.csv` �������� `./data` ��
  
* #### �������ѵ��ģ��

    `python App.py [-h] train_filepath test_filepath`

    `train_filepath` ��ѵ������������·��

    `test_filepath`�����Լ���������·��

    `python App.py ./data/train.csv ./data/test.csv`

* #### ����������ģ�Ͳ�����������������������ģ�����������׼ȷ��



## TODO
��ǰ��ֱ���������ϵͳ�ϸ��֣���Ϊ�˱��ں���ά��Ǩ�ƣ�����Ӧ�ý����ֵ�©����������Ž�docker��

��ǰ���ݵ�Ԥ������ֱ�Ӷ�ȡ.log�ļ�����Ϊ.csv��������ץ��Apache������.pcap������תΪתΪ.json����Ԥ����תΪ.csv������ʣ�