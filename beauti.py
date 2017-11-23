from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

html = urlopen("https://time100.ru/Moscow")

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		str_out_pars = str(bsObj.findAll("div", {"class":"time","data-tz":"Europe/Moscow"})[0])
		ugly_result = str_out_pars.split(">")[1]
		result = ugly_result.split("<")[0]
	except AttributeError as e:
		return None
	return result

result = getTitle("https://time100.ru/Moscow")
if result == None:
	print("Результат не найден")
else:
	print('Точное московское время-->',result)

# html = urlopen("https://time100.ru/Moscow")
# bsObj = BeautifulSoup(html.read(),"html.parser")
# str_out_pars = str(bsObj2.findAll("div", {"class":"time","data-tz":"Europe/Moscow"})[0])
# ugly_result = str_out_pars.split(">")[1]
# result = ugly_result.split("<")[0]
# print('Точное московское время-->',result)
