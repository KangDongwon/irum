import urllib

# 요청
result = urllib.request.urlopen('http://irum.dothome.co.kr/test.html')

if result.status != 200 : # 실패 응답
    print(f'Response Failed : {result.status}, {result.reason}') # 에러 메시지 출력
else : # 성공 응답
    html = result.read().decode()

    # 변수 만들기
    start = 0  # 0번째 인덱스부터 시작
    stack = [] # 태그의 짝을 맞추기 위한 스택
    success = True # html 파싱 결과의 성공 여부
    text = '' # html 파싱 결과 태그를 제외한 텍스트만 추출하여 저장할 변수

    while True : 
        pos_open = html.find('<', start) # 태그 시작
        pos_close = html.find('>', pos_open+1) # 태그 끝
        if  : # 못 찾으면 종료
            break
        elif  : # <! 로 시작하는 태그 무시
            start = pos_open + 1
        elif : # </ 로 시작하는 태그는 닫는 태그, 태그 끝도 있으면
            tag =  # 닫는 태그 이름을 구하고
            if  : # 스택에서 여는 태그를 하나 꺼내어 비교 후 다르면 오류 처리
                success = False
                break
            start = pos_open + 1 # 다음 탐색할 위치 지정
        elif  : # < 로 시작하는 여는 태그이고 태그 끝이 있으면 
            tag =  # 여는 태그 이름을 구하고
            value =  # 그 다음 태그 시작까지가 텍스트값

            # 파싱 내용을 출력
            tab = '\t'*len(stack)
            print(f'{tab}{tag} : {value}')
            
            text =  # 위에서 구한 텍스트값을 변수에 저장
                    # 여는 태그는 스택에 넣는다
            start = pos_open + 1 # 다음 탐색할 위치 지정
        else : # 위 조건에 걸리지 않으면 < > 가 안 맞는 것이므로 오류 처리
            success = False
            break

    if success == False :
        print('html parsing error!') #에러 출력
    else :
        print('OK!')# 성공 출력
        print()     # 빈줄 출력
        print(text) # 추출한 텍스트값 출력