# -*- coding: utf-8 -*-
import urllib2, base64, json




def call_rest_api_of_gitbook(path):
	# Basic Auth. 
	# https://developer.gitbook.com/authentication/basic.html
	basic_url = 'https://api.gitbook.com/'
	# username
	username = ''
	# token: Account Setting -> Applications/Tokens: API Token
	token = '' 
	url = "%s%s" %(basic_url, path)
	request = urllib2.Request(url)
	base64string = base64.encodestring('%s:%s' % (username, token)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   
	result = urllib2.urlopen(request)
	data = result.read()
	jdata = json.loads(data)
	print data
	print jdata

def main():
	# /topics
	url = '/topics'
	call_rest_api_of_gitbook(url)
	
if __name__ == '__main__':
	main()