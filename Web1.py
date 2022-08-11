#Web1.py

#웹크롤링(데이터 수집)
from traceback import print_tb
from bs4 import BeautifulSoup

#메서드 체인 : 연속으로 함수나 메서드 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser") #옵션이 4가지가 있음
#print(soup.prettify())

#<p>태그 몽땅 검색
#print(soup.find_all("p"))

#첫번째 p태그만 검색
#print(soup.find("p"))

#조건이 있는: <p class='outer-test')
#파이썬 키워드 class => class_
#print(soup.find_all("p", class_="outer-text"))

#내부 문자열 추출
for item in soup.find_all("p"):
    #컨텐츠: ~.text 
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)
