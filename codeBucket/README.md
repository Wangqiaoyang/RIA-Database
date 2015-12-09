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


##特定帖子中的内容转Markdown格式

以帖子http://www.douban.com/group/topic/79588017/ 为例，将楼主的回复转为Markdown格式，写入test.md中。
测试命令为：```scrapy crawl testspider```
