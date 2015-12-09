# -*- coding: utf
import re
import scrapy
import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class GroupSpider(scrapy.Spider):
    name = 'groupspider'
    allowed_domains = ["douban.com"]
    start_urls=[
    "http://www.douban.com/group/562894/discussion"
    ]

    
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
        
    
    
        