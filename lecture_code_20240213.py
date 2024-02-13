def main() :
    while True :
        # 화면과 같은 메시지를 출력하도록 코드를 작성하세요.


        # 화면과 같은 메뉴를 출력하도록 코드를 작성하세요.


        # 메뉴를 입력받도록 코드를 작성하세요.
        s = 

        if s == '1' : #login
            # 로그인할 ID를 입력받도록 코드를 작성하세요.
            x = 
            try :
                # Member.txt 파일을 읽기모드로 열도록 코드를 작성하세요.
                f = 
                while True :
                    # 위에서 연 파일로부터 한 라인씩 읽도록 코드를 작성하세요.
                    line = 
                    # 위에서 읽어들인 문자열로부터 줄바꿈(\n) 문자열을 제거해 보세요.
                    line = 
                    
                    if line == x :
                        print(f'{x}님 환영합니다.')
                        break
                    elif lien == '' :
                        print('가입되지 않은 ID입니다.')
                        break

            except FileNotFoundError :
                f = None
            except :
                print('파일 처리 오류!')
            finally :
                if f != None :
                    f.close()

        elif s == '2' : #join
            # 가입할 ID를 입력받도록 코드를 작성하세요.
            x = 
            try :
                # Member.txt 파일을 이어쓰기모드로 열도록 코드를 작성하세요.
                f = 
                # 위에서 연 파일에 입력받은 ID를 쓰도록 코드를 작성하세요.
                # 아이디 뒤에 줄바꿈 문자가 포함되어야 합니다.
                
            except :
                print('파일 처리 오류!')
            else :
                print(f'{x}님 가입되었습니다.')
            finally :
                f.close()
                
        elif s == '3' : #exit
            print('종료합니다.')
            break
        else :
            print('원하는 메뉴를 입력하세요.')

main()