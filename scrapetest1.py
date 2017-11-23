from urllib.request import urlopen as op
html = op("http://pythonscraping.com/pages/page1.html")
html2 = op("http://finc8888.pythonanywhere.com")
html3 = op("https://time100.ru/Moscow")
#print(html.read())
#print(html2.read())
print(html3.read()) 
