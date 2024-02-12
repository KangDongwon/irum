def input_name() :
    while True :
        name = input('이름 : ')
        if  : #조건문을 작성해 보세요.
            break
        else :
            print('이름은 3글자이어야 합니다.')

    return name

def input_birth() :
    while True :
        birth = input('생일과 주민번호뒤1자리 : ')
        if  : #조건문을 작성해 보세요.
            break
        else :
            print('형식에 맞지 않습니다. 000000-0 숫자로 입력해주세요.')

    return birth

def calculate_age(birth) :
    #birth 에는 000000-0 형식의 문자열이 들어가있음
    if birth[7] == '1' or birth[7] == '2' :
        #조건에 맞는 birth_year 문자열을 완성해 보세요.
    elif birth[7] == '3' or birth[7] == '4' :
        #조건에 맞는 birth_year 문자열을 완성해 보세요.

    age = 2024 - int(birth_year) + 1
    return age

def get_gender(birth) :
    #birth 에는 000000-0 형식의 문자열이 들어가있음
    if  : #조건문을 작성해 보세요.
        gender = '남성'
    elif  : #조건문을 작성해 보세요.
        gender = '여성'

    return gender

def print_member_info(member) :
    #화면과 같은 메시지를 출력해 보세요.

    name, birth = member.split(',')
    #예시와 같이 회원정보를 출력해보세요.


def go_login() :
    #화면과 같은 메시지를 출력해 보세요.

    #이름을 입력받아 반환하는 함수를 호출하도록 코드를 작성하세요.
    name = 
    #입력받은 이름을 인자로 하여 회원을 찾아 반환하는 함수를 호출하도록 코드를 작성하세요.
    member = 

    if member == '' :
        print(f'{name} 회원은 존재하지 않습니다.')
    else :
        #회원을 인자로 하여 회원정보를 출력하는 함수를 호출하도록 코드를 작성하세요.
        

def find_member(name) :
    try :
        #Member.txt 파일을 읽기 모드로 여는 코드를 작성하세요.
        
        while True :
            line = f.readline()
            if line == '' :
                break
            else :
                f_name,f_birth = line.split(',')
                if name == f_name :
                    break
    except FileNotFoundError :
        line = ''
        f = None
    except :
        print('find_member : 파일 처리 오류!')
    finally :
        if f != None :
            f.close()

    return line

def save_member(name, birth) :
    try :
        #Member.txt 파일을 이어쓰기 모드로 여는 코드를 작성하세요.
        
        #위에서 연 파일에 회원정보를 저장하는 코드를 작성하세요.
        
    except :
        print('save_member : 파일 처리 오류!')
    else :
        print(f'{name}님 회원가입되었습니다.')
    finally :
        f.close()

def go_join() :
    #화면과 같은 메시지를 출력해 보세요.

    while True :
        #이름을 입력받아 반환하는 함수를 호출하도록 코드를 작성하세요.
        name = 
        #입력받은 이름을 인자로 하여 회원을 찾아 반환하는 함수를 호출하도록 코드를 작성하세요.
        member = 

        if member == '' :
            #생일을 입력받아 반환하는 함수를 호출하도록 코드를 작성하세요.
            birth = 
            #입력받은 이름과 생일을 인자로 하여 회원 정보를 저장하는 함수를 호출하도록 코드를 작성하세요.
            
            break
        else :
            print(f'{name} 회원은 이미 가입되어 있습니다.')

def main() :
    while True :
        #화면과 같은 메시지를 출력해 보세요.

        #화면과 같은 메시지를 출력해 보세요.

        choice = input('메뉴를 선택하세요. : ')
        if choice == '1' :
            #메뉴에 맞는 함수를 호출하도록 작성해 보세요.
        elif choice == '2' :
            #메뉴에 맞는 함수를 호출하도록 작성해 보세요.
        elif choice == '3' :
            print('종료합니다.')
            break
        else :
            print('원하는 메뉴를 입력하세요.')

main()