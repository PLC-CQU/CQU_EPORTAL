# cqu_web_login

#### 介绍
适用于重庆大学（虎溪校区） linux服务器的上网登陆python脚本

#### 使用方式

##### 1. 准备工作，安装脚本中使用的 python 包（如果已安装这些包，则跳过该步骤）
```shell
pip3 install requests

pip3 install urllib

pip3 install sys

pip3 install subprocess

pip3 install psutil

pip3 install socket
```
##### 2. 执行下面的命令（用户名和密码建议带上单引号， 防止密码中的字符在shell中有特殊含义）

```shell
git clone https://gitee.com/nullzx/cqu_web_login.git  ~/cqu_web_login
```

* login
```shell
python3  ~/cqu_web_login/eportal.py  login  '用户名'     '密码'
```
* logout
```shell
python3 ~/cqu_web_login/eportal.py  logout
```
