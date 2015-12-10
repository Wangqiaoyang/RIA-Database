# -*- coding: utf
import re
import html2text
import scrapy
import BeautifulSoup
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class GroupSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ["douban.com"]
    file = open('discussion_list.txt', 'r')
    start_urls = []
    for line in file.readlines():
    	start_urls.append(line.strip('\n'))
    	
    
    def parse(self, response):
    	filename = "topic/topic_"+response.url.split('/')[-2]
    	sel=Selector(response)
    	a = sel.xpath('//*[@id="link-report"]/div[1]').extract()[0]
    	
    	file = open(filename+'.md', 'wb')
    	h = html2text.HTML2Text()
    	text =  h.handle(a)
    	file.write(text.encode("utf8"))
    	file.close()
    
    
    
        