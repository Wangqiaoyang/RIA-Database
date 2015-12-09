# -*- coding: utf
import re
import html2text
import scrapy
import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class GroupSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ["douban.com"]
    start_urls=[
    #"http://www.douban.com/group/topic/81573808/",
    #"http://www.douban.com/group/topic/81959306/",
    "http://www.douban.com/group/topic/79588017/"
    ]
    
    def parse(self, response):
    	sel=Selector(response)
    	a = sel.xpath('//*[@id="link-report"]/div[1]').extract()[0]
    	file = open('test.md', 'wb')
    	h = html2text.HTML2Text()
    	text =  h.handle(a)
    	file.write(text.encode("utf8"))
    	file.close()
    
"""    
    def makelist(self, table):
    	result = []
    	allrows = table.findAll('tr')
    	for row in allrows:
    		result.append([])
    		allcols = row.findAll('td')
    		tmp = allcols[0].findAll('a')
    		if tmp != []:
    			href = tmp[0].get("href")
    			title = tmp[0].get("title")
    			result[-1].append(href)
    			result[-1].append(title)
    	return result
    
    def parse(self, response):
        sel=Selector(response)
        a = sel.xpath('//*[@id="content"]/div/div[1]/div[2]/table').extract()
        
        print
        for i in a:
        	html = i.encode("utf8")
        	soup = BeautifulSoup.BeautifulSoup(html)
        	for item in self.makelist(soup.findAll('table')[0]):
        		if item == []:
        			continue
        		print item[0], item[1]
        print
        
        nextlink = sel.xpath('//*[@id="content"]/div/div[1]/div[3]/span[3]/link').extract()
        if nextlink :
        	soup = BeautifulSoup.BeautifulSoup(nextlink[0])
        	next = soup.findAll('link')[0].get("href")
        	yield scrapy.Request(response.urljoin(next),callback=self.parse ) 
"""   
    
    
        