from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
html2 = urlopen("http://finc8888.pythonanywhere.com")
html3 = urlopen("https://time100.ru/Moscow")
bsObj = BeautifulSoup(html.read(),"html.parser")
bsObj1 = BeautifulSoup(html2.read(),"html.parser")
bsObj2 = BeautifulSoup(html3.read(),"html.parser")
# print(bsObj.h1)
# print(bsObj1.h1)
str_out_pars = str(bsObj2.findAll("div", {"class":"time","data-tz":"Europe/Moscow"})[0])
# print(list_pars)
ugly_result = str_out_pars.split(">")[1]
result = ugly_result.split("<")[0]
print(result)

# def getTitle(url):
# 	try:
# 		html = urlopen(url)
# 	except HTTPError as e:
# 		return None
# 	try:
# 		bsObj = BeautifulSoup(html.read(),"html.parser")
# 		title = bsObj2.findAll("div", {"class":"time","data-tz":"Europe/Moscow"})[0].split(">")
# 	except AttributeError as e:
# 		return None
# 	return title
# title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
# if title == None:
# 	print("Title could not be found")
# else:
# 	print(title)
# title = getTitle("https://time100.ru/Moscow")
# if title == None:
# 	print("Title could not be found")
# else:
# 	print(title)
