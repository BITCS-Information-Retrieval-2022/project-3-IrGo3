## 环境配置说明

### 1. 创建并开启mongoDB副本集

https://www.pudn.com/news/6305f30476296c16d32cd777.html

### 2. 将paper、video、ppt、ebook的爬虫数据保存至数据库IR下，结构如下

![image-20221220230519608](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20221220230519608.png)

### 3. 创建视图，对应./config/createView.txt文件

```
# mongo
rs0:PRIMARY> use IR
rs0:PRIMARY> db.createView("paperView", "paper", [{$project: {"id": 1, "title": 1, "published": 1, "authors": 1}}])
rs0:PRIMARY>db.createView("videoView", "video", [{$project: {"bvid": 1, "title": 1, "description": 1}}])
rs0:PRIMARY>db.createView("pptView", "ppt", [{$project: {"title": 1, "paper": 1}}])
rs0:PRIMARY>db.createView("ebookView", "ebook", [{$project: {"id": 1, "title": 1, "authors": 1, "on_sale_date": 1}}])
```

### 4. 创建es索引，对应./config/...sh文件

删除原有索引，并创建新索引

```
bash build_paper.sh
bash build_video.sh
bash build_ppt.sh
bash build_ebook.sh
```

### 5. 安装monstache并配置相关文件，对应./config/config.toml

配置文件位于./monstache-9e60b1d/build/windows-amd64路径下

### 6. 执行monstache，实现mongodb与elasticSearch数据同步

```
monstache -f config.toml
```

