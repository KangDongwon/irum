import urllib
from bs4 import BeautifulSoup

# 요청
result = urllib.request.urlopen('http://irum.dothome.co.kr/test.html')

if result.status != 200 : # 실패 응답
    print(f'Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
else : # 성공 응답
    soup = BeautifulSoup(result.read(), 'html.parser')

    # 실습 1 : html 태그 찾아서 출력
    #root = soup.find('html')
    #print(root.text)

    # 실습 2 : p 태그 찾아서 출력
    #print(soup.find('p'))
    #print(soup.find_all('p'))

    # 실습 3 : article 자식 태그 출력
    #for child in soup.find('article').children :
    #    if child != '\n' :
    #       print(child)

    # 실습 4 : h5 부모 태그 출력
    #print(soup.find('h5').parent.name)

    # 실습 5 : p 태그 찾아서 출력
    #print(soup.select_one('p'))
    #print(soup.select('p'))

    # 실습 6 : article 자식 태그 출력
    #for child in soup.select_one('article').children :
    #    if child != '\n' :
    #       print(child)

    # 실습 7 : h5 부모 태그 출력
    #print(soup.select_one('h5').parent.name)