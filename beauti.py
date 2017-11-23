from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
html2 = urlopen("http://finc8888.pythonanywhere.com")
html3 = urlopen("https://time100.ru/Moscow")
bsObj = BeautifulSoup(html.read(),"html.parser")
bsObj1 = BeautifulSoup(html2.read(),"html.parser")
bsObj2 = BeautifulSoup(html3.read(),"html.parser")
print(bsObj.h1)
print(bsObj1.h1)
print(bsObj2.findAll("div", {"data-tz":"Europe/Moscow"}))

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
