# -*- coding: utf
import re
import scrapy
import BeautifulSoup
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class GroupSpider(scrapy.Spider):
    name = 'groupspider'
    allowed_domains = ["douban.com"]
    start_urls=[
    "http://www.douban.com/group/562894/discussion"
    ]
    
    discussion_list = []
    
    
    def parse(self, response):
        sel=Selector(response)
        rows = sel.xpath('//*[@class="olt"]/tr')
        for row in rows:
        	discuss_title = row.xpath('.//*[@class="title"]/a/text()').extract()
        	discuss_title_href = row.xpath('.//*[@class="title"]/a/@href').extract()
        	if discuss_title_href:
        		self.discussion_list.append(discuss_title_href[0])
                
        nextlink = sel.xpath('//*[@class="next"]/a/@href').extract()
        if nextlink :
        	link = nextlink[0]
        	yield scrapy.Request(response.urljoin(link),callback=self.parse)
        else:
        	file = open('discussion_list.txt', 'wb')
        	for url in self.discussion_list:
        		file.write(url+"\n")
        	file.close()
        
        
    
    
        