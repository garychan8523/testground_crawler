import requests
# from bs4 import BeautifulSoup
import re

session = requests.Session()
# print(session.cookies.get_dict())
response1 = session.get('http://www.urbtix.hk/')
response2 = session.get('https://ticket.urbtix.hk/internet/eventSearch/dateCode/20170808')
# print(session.cookies.get_dict())
#r = requests.get('https://ticket.urbtix.hk/internet/eventSearch/dateCode/20170808')
response2.encoding = 'utf-8'
result = response2.text
start = -1
end = -1
for match in re.finditer('eventListJSON', result):
    start = match.start()
end = start
while (result[end] != ';' and (end < len(result))):
	end += 1

if(start != -1 and end != -1):
	# print('start: ' + str(start))
	# print('end: ' + str(end))
	# print(result[start:end])
	print(result[start+16:end])
else:
	print('not found')


##############################################################
# for browser similation, ensure js generate content be seen
# from selenium import webdriver
# 
# driver = webdriver.PhantomJS(executable_path=r'/Users/garychan/phantomjs/bin/phantomjs')
# driver.get('https://ticket.urbtix.hk/internet/eventSearch/dateCode/20170808')
# pageSource = driver.page_source
# print(pageSource)
# 
# driver.close()
