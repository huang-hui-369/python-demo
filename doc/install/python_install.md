# download python

https://www.python.org/downloads

![](img\2021-05-07-15-00-34.png)

ダブルクリックダウンロードしたファイル、pythonをインストールします。


# python 確認
以下のコマンドを実行してpython正しくインストールされたことを確認する。
```
C:\Users\D2019-06>python -V

Python 3.9.5

```

# install django
pythonがインストールされた後で、以下のコマンドを実行して、Djangoをインストールします。

```
$ python -m pip install Django
```

# django 確認

```
py -m django --version
3.2.2

```
or type py in comand console
```
>>> import django
>>> print(django.get_version())
3.2
>>> django
<module 'django' from 'D:\\Python39\\lib\\site-packages\\django\\__init__.py'>

```
由此可知django安装在 d:\Python39\lib\\site-packages\\django目录

![](img\2021-05-07-16-52-52.png)


# uninstall django

```
pip uninstall django
```

# create virtual env

什么叫虚拟环境，这是为了区别全局系统环境，全局系统环境是所有项目共通使用的环境。
全局系统环境目录如下
d:\Python39
虚拟环境是为了项目之间互相不影响，干扰，可以根据不同的项目创建不同的虚拟环境，因为每个项目使用了不同的版本的库。

## 查看系统环境现状

*  pip list 
    ```
    D:\>pip list
    Package    Version
    ---------- -------
    asgiref    3.3.4
    Django     3.2.2
    pip        21.1.1
    pytz       2021.1
    setuptools 56.0.0
    sqlparse   0.4.1

    ```
* py -m pip freeze    

    ```
    D:\>py -m pip freeze
    asgiref==3.3.4
    Django==3.2.2
    pytz==2021.1
    sqlparse==0.4.1

    ```

## create venv

https://docs.python.org/zh-cn/3/library/venv.html

通过命令 py -m venv venv 可以创建一个虚拟环境

以下的命令就会正在目录D:\github\python-demo\django-demo中创建一个虚拟环境。
```
cd D:\github\python-demo\django-demo
py -m venv .venv
```

会创建出以下目录和文件

![](img\2021-05-10-18-24-41.png)

pyvenv.cfg文件定义了Python版本。

```
home = D:\Python39
include-system-site-packages = false
version = 3.9.5

```

## 激活 venv
执行Script目录下的 activate

![](img\2021-05-10-18-26-04.png)

```

cd D:\github\python-demo\django-demo\.venv\Scripts
activate

```

![](img\2021-05-10-18-28-40.png)
当一个虚拟环境被激活时，VIRTUAL_ENV 环境变量会被设为该虚拟环境的路径。 这可被用来检测程序是否运行在虚拟环境中。

```
(django-demo) D:\github\python-demo\django-demo>echo %VIRTUAL_ENV%
D:\github\python-demo\django-demo\.venv

```

## install package

执行 py -m pip install Django 用来安装 Django

![](img\2021-05-07-17-07-01.png)

可以看出 Django 安装在了项目的虚拟环境中了D:\github\python-demo\django-demo\Lib\site-packages

![](img\2021-05-07-17-12-04.png)


## 退出 venv

执行命令 deactivate


![](img\2021-05-07-17-14-09.png)


## 生成 requirements.txt

pip freeze > requirements.txt

## powershellでvenv環境を構築する

まず管理者権限でpowershellを起動し以下のコマンドを実行することでスクリプトファイルが実行できるようにする

```
PS > PowerShell Set-ExecutionPolicy RemoteSigned
```
次に対象のローカルファイルでvenvファイルの作成

```
PS > python -m venv venv
```
次に仮想環境の起動

```
PS > venv\Scripts\activate.ps1
```
出るときは

```
PS > deactivate
```