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
    	#break
    	
    
    def parse(self, response):
    	filename = "topic/topic_"+response.url.split('/')[-2]
    	sel=Selector(response)
    	from_user = sel.xpath('//*[@class="topic-doc"]/h3/span[1]/a/text()').extract()[0]
    	from_user_href = sel.xpath('//*[@class="topic-doc"]/h3/span[1]/a/@href').extract()[0]
    	pubtime = sel.xpath('//*[@class="topic-doc"]/h3/span[2]/text()').extract()[0]
    	from_user =  "###" + "[" + from_user + "]" + "(" + from_user_href + ")" + "\t" + pubtime + "\n"
    	
    	title = self.handle_title(sel.xpath('//*[@id="content"]/h1/text()').extract());
    	reply_docs = self.handle_comments(sel.xpath('//*[@class="reply-doc content"]'))
    	a = sel.xpath('//*[@id="link-report"]/div[1]').extract()[0]
    	file = open(filename+'.md', 'wb')
    	h = html2text.HTML2Text()
    	text =  h.handle(a)
    	file.write(title.encode("utf8") + "\n---\n")
    	file.write(from_user.encode("utf8"))
    	file.write(text.encode("utf8"))
    	for reply in reply_docs:
    		file.write(reply.encode("utf8"))
    	file.close()
    
    def handle_title(self, list):
    	headline = list[0].strip('\n').lstrip(' ')
    	return "#" + headline
    
    def handle_comments(self, comments):
    	replys = []
    	for comment in comments:
    		herf = comment.xpath('.//div[1]/h4/a/@href').extract()[0]
    		username = comment.xpath('.//div[1]/h4/a/text()').extract()[0]
    		pubtime = comment.xpath('.//div[1]/h4/span/text()').extract()[0]
    		reply = html2text.HTML2Text().handle(comment.xpath('.//p').extract()[0])
    		title = "---\n###" + "[" + username + "]" + "(" + herf + ")" + "\t" + pubtime + "\n"
    		replys.append(title + reply)
    	return replys