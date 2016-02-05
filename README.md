# remote_cdp

To use remote cdp feature, first setup management interface and enable scp-server & nxapi feature

#Setup python environment, 
Install python-pip  #sudo apt-get install python-pip on Ubunut/Debian and #sudo yum install python-pip on RHEL/CentOS/SUSE. 
After installation of pip, 
\#sudo pip install paramiko scpclient 

#How to do execute remote_cdp on your Linux/MacOS 
1. add hosts on hosts.yaml 
2. export NEXUS_USERNAME and NEXUS_PASSWD  ( ex, export NEXUS_USERNAME=admin ; export NEXUS_PASSWD=cisco) 
3. #python nxapi_remote_cdp.py hosts.yaml 


#How it works
remote_cdp copy update_cdp.py on Nexus device on /bootflash 
and execute python bootflash:update_cdp.py via NXAPI 

update_cdp.py maintains user's description and connectivity information.
For keeping user description  just add ":" after description.
For example 
\#conf t;
(config)#interfac eth1/1
(config-if)#desc this_is_my_desc : 

update_cdp.py only add link information after : if exist on currernt description.

Happy management with Cisco Nexus programmability 
