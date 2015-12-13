# 豆瓣小组爬虫Demo

## 依赖包
需要手动安装一下依赖包。

```
html2text
scrapy
```

## 运行

默认在`brainTruster/topic`路径下存放每个帖子的`Markdown`文件，因此需要手动创建这个目录。如果需要重定义路径，修改`groupspider.py`中的`topic_path`变量即可。

运行方法：

1. 在`brainTruster`执行`scrapy crawl groupspider`即可
2. 执行`python generate_summary.py`生成目录

