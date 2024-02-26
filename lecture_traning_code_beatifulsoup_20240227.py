import urllib
from bs4 import BeautifulSoup

# 블로그 게시글 URL 요청
result = urllib.request.urlopen('https://blog.naver.com/irum_com/223332645529')

if result.status != 200 : # 실패 응답
    print(f'Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
else : # 성공 응답
    soup = BeautifulSoup(result.read(), 'html.parser')
    # 블로그 본문 URL 구하기
    body_url = 'https://blog.naver.com' + soup.iframe['src']

    # 블로그 본문 URL 요청
    result = urllib.request.urlopen(body_url)

    if result.status != 200 : # 실패 응답
        print(f'Body Url Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
    else : # 성공 응답
        soup = BeautifulSoup(result.read(), 'html.parser')
        # 블로그 본문 태그 
        body = soup.find('div', 'se-main-container')
        
        body_text = body.text.replace('\n','')
        print(body_text)

        with open('blog.txt', 'a') as f :
            f.write(body_text)