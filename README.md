# Irgogogo学术搜索引擎——中文简介

## 概况
详情请见`信息检索课程答辩.PPT`

## 项目配置
详见config文件夹的readme

## 运行步骤 
1. 启动数据库，详见config文件夹的readme
2. 启动Elasticsearch，详见config文件夹的readme
3. 启动服务器
启动虚拟环境: activate miniSearchEngine
进入server目录: python main.py
4. 启动客户端
进入engine_front目录: npm run serve

# Irgogogo scientific search engine —— English version

## Introduction
Our project contains mainly 5 parts,that is webcrawler,
1. we have to admit that the webcrawler is not very powerful but merely for collect data process.
2. The project now is merely a demo with projects.
 
Please refer to the `信息检索课程答辩.PPT`

## Configuration in windows
For details please refer to the `readme` in `config` file folder

## Runing process
1. start the two replica of the database:please refer to the `readme` in `config` folder
2. start Elasticsearch:please refer to the `readme` in `config` folder
3. start the server:

- first install the dependencies of the server part,do the following instructions:
```python
conda create -n minisearch python=3.7
conda install flask==2.0.2
conda install flask_cors==3.0.8
conda install elasticsearch==7.0.4
conda install pymongo==3.12.0
```
* notice the flask package installation probably have some problem; 
* the total dependent package are listed below,if some packages conflict, please check the version again.Notice the package includes scrapyelasticsearch and scrapy which is for the webcrawler and not used here.

```shell
attrs                     22.1.0                   pypi_0    pypi
automat                   22.10.0                  pypi_0    pypi
ca-certificates           2022.10.11           haa95532_0
certifi                   2022.12.7        py37haa95532_0
cffi                      1.15.1                   pypi_0    pypi
click                     8.1.3                    pypi_0    pypi
colorama                  0.4.6                    pypi_0    pypi
constantly                15.1.0                   pypi_0    pypi
cryptography              38.0.4                   pypi_0    pypi
cssselect                 1.2.0                    pypi_0    pypi
elasticsearch             7.0.4                    pypi_0    pypi
flask                     2.0.2                    pypi_0    pypi
flask-cors                3.0.8                    pypi_0    pypi
hyperlink                 21.0.0                   pypi_0    pypi
idna                      3.4                      pypi_0    pypi
importlib-metadata        5.1.0                    pypi_0    pypi
incremental               22.10.0                  pypi_0    pypi
itsdangerous              2.1.2                    pypi_0    pypi
jinja2                    3.0.3                    pypi_0    pypi
lxml                      4.9.1                    pypi_0    pypi
markupsafe                2.1.1                    pypi_0    pypi
openssl                   1.1.1s               h2bbff1b_0
packaging                 21.3                     pypi_0    pypi
parsel                    1.7.0                    pypi_0    pypi
pip                       22.2.2           py37haa95532_0
pyasn1                    0.4.8                    pypi_0    pypi
pyasn1-modules            0.2.8                    pypi_0    pypi
pycparser                 2.21                     pypi_0    pypi
pydispatcher              2.0.6                    pypi_0    pypi
pyhamcrest                2.0.4                    pypi_0    pypi
pymongo                   3.12.0           py37hd77b12b_0
pyopenssl                 22.0.0                   pypi_0    pypi
pyparsing                 3.0.9                    pypi_0    pypi
python                    3.7.15               h6244533_1
queuelib                  1.6.2                    pypi_0    pypi
scrapy                    1.6.0                    pypi_0    pypi
scrapyelasticsearch       0.9.1                    pypi_0    pypi
service-identity          21.1.0                   pypi_0    pypi
setuptools                65.5.0           py37haa95532_0
six                       1.16.0                   pypi_0    pypi
sqlite                    3.40.0               h2bbff1b_0
twisted                   20.3.0                   pypi_0    pypi
twisted-iocpsupport       1.0.2                    pypi_0    pypi
typing-extensions         4.4.0                    pypi_0    pypi
urllib3                   1.26.13                  pypi_0    pypi
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
w3lib                     2.1.0                    pypi_0    pypi
werkzeug                  2.2.2                    pypi_0    pypi
wheel                     0.37.1             pyhd3eb1b0_0
wincertstore              0.2              py37haa95532_2
zipp                      3.11.0                   pypi_0    pypi
zope-interface            5.5.2                    pypi_0    pypi
```
- in the conda prompt ,do `activate minisearch`
- run `cd backend` to switch to  the `backend` folder, and just run `python main.py`

4. start the client(frontend):
- first make sure you have installed the nodejs, and able to use `npm`;
- run `npm install` to install the dependencies;  
- run `cd engine_front` to switch to  the `engine_front` folder, and just run `npm run serve`

