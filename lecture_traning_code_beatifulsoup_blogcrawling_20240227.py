import urllib
from bs4 import BeautifulSoup

# 블로그의 글 목록 URL
url = 'https://blog.naver.com/PostList.naver?from=postList&blogId=irum_com&categoryNo=41&currentPage='

url_list = []

for i in range(1,11) :
    req_url = f'{url}{i}'
    result = urllib.request.urlopen(req_url)

    if result.status != 200 : # 실패 응답
        print(f'Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
    else : # 성공 응답
        soup = BeautifulSoup(result.read(), 'html.parser')

        item_list = soup.find('ul', 'thumblist').find_all('li')

        for href in item_list :
            url_list.append(href.find("a")["href"])
            #print(href.find("a")["href"])
        
for url in url_list :
    # 블로그 게시글 URL 요청
    result = urllib.request.urlopen(f'https://blog.naver.com{url}')

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

        with open('blog_irum.txt', 'a') as f :
            f.write(body_text)