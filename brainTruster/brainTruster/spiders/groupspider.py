# -*- coding: utf
import scrapy
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
    
    topic_path = 'topic'
    
    def parse_discussion(self, response):
    	pass
    
    def parse(self, response):
    	sel=Selector(response)
    	rows = sel.xpath('//*[@class="olt"]/tr')
        for row in rows:
        	discuss_title = row.xpath('.//*[@class="title"]/a/text()').extract()
        	discuss_title_href = row.xpath('.//*[@class="title"]/a/@href').extract()
        	if discuss_title_href:
        		self.discussion_list.append(discuss_title_href[0])
		
		# check if there is next page.
        nextlink = sel.xpath('//*[@class="next"]/a/@href').extract()
        if nextlink :
        	link = nextlink[0]
        	# get url of next page, and call parse to process it.
        	yield scrapy.Request(response.urljoin(link),callback=self.parse)
        else:
        	# all discussion topics have been crawled. start to process every topic.
        	for discussion in self.discussion_list:
        		yield scrapy.Request(response.urljoin(discussion),callback=self.parse_discussion)  	
    
        