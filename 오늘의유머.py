# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#웹서버에서 웹봇을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #오늘의 유머 주소
        data = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()

        #혹시 한글이 깨져 있을 경우 다시 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=458356&amp;s_no=458356&amp;page=1" target="_top">\
        # "김건희 여사 숙대 석사 논문 표절률 최대 54.9%"</a>
        list = soup.findAll('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.find("a").text
                        #print(title.strip())
                        if (re.search('김건희', title)):
                                print(title.strip())
                                #print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
