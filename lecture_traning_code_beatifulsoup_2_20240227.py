import urllib
from bs4 import BeautifulSoup

# 블로그 게시글 URL 요청
result = urllib.request.urlopen('https://blog.naver.com/PostView.naver?blogId=irum_com&logNo=223332645529&categoryNo=41&parentCategoryNo=&from=thumbnailList')

if result.status != 200 : # 실패 응답
    print(f'Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
else : # 성공 응답
    soup = BeautifulSoup(result.read(), 'html.parser')
    # 블로그 본문 태그 
    if soup.find('div', 'se-main-container') :
        body = soup.find('div', 'se-main-container')
        #print('body tag se-main-container')
    elif soup.find('div', id = 'postViewArea') :
        body = soup.find('div', id = 'postViewArea')
        #print('body tag postviewarea')
    else :
        print('cannot find body tag!')

    body_text = body.text.replace('\n','')
    print(body_text)

    with open('blog.txt', 'a') as f :
        f.write(body_text)