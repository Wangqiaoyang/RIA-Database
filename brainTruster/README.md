# 豆瓣小组爬虫Demo

## 依赖包
需要手动安装一下依赖包。

```
html2text
BeautifulSoup
scrapy
```

## 获取小组帖子列表

在```tutorial```目录执行：```scrapy crawl groupspider```

帖子列表会在CLI中打印，尚未写入文件中。测试时注意查看。


##帖子内容转Markdown格式

在```tutorial```目录下新建一个```topic```目录，然后执行如下命令：

```scrapy crawl testspider```

在topic目录下，以topic id作为文件名，生成小组内所有帖子的md文件
