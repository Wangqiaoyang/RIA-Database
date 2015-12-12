# -*- coding: utf
import os,sys
import scrapy
import html2text
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
        	# make sure the path to store topic markdown file exist.
        	if not os.path.exists(self.topic_path):
        		msg = "\n\nERROR: Directory %s doesn't exit. Please check it again.\n" 
        		sys.exit(msg % self.topic_path)
        		
        	for discussion in self.discussion_list:
        		yield scrapy.Request(response.urljoin(discussion),callback=self.parse_discussion)
    
    def parse_discussion(self, response):
    	filename = self.topic_path + "/topic_"+response.url.split('/')[-2]
    	sel=Selector(response)
    	
    	title = self.handle_title(sel.xpath('//*[@id="content"]/h1/text()').extract())
    	from_user = self.handle_fromuser(sel)
    	
    	
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
    
    def handle_fromuser(self, sel):
    	from_user = sel.xpath('//*[@class="topic-doc"]/h3/span[1]/a/text()').extract()[0]
    	from_user_href = sel.xpath('//*[@class="topic-doc"]/h3/span[1]/a/@href').extract()[0]
    	pubtime = sel.xpath('//*[@class="topic-doc"]/h3/span[2]/text()').extract()[0]
    	result =  "###" + "[" + from_user + "]" + "(" + from_user_href + ")" + "\t" + pubtime + "\n"
    	return result
    
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
        