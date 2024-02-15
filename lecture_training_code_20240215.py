def calculate_age(birth) :
    if birth[7] == '1' or birth[7] == '2' :
        birth_year = '19' + birth[0:2]
    elif birth[7] == '3' or birth[7] == '4' :
        birth_year = '20' + birth[0:2]

    age = 2024 - int(birth_year) + 1
    return age

def get_birthday(birth) :
    month = str(int(birth[2:4]))
    day = str(int(birth[4:6]))
    birthday = f'{month}월 {day}일'
    return birthday

def get_gender(birth) :
    if birth[7] == '1' or birth[7] == '3' :
        gender = '남성'
    elif birth[7] == '2' or birth[7] == '4' :
        gender = '여성'

    return gender

def input_name() :
    while True :
        name = input('이름(3글자) : ')
        if len(name) == 3 and name.isalpha() :
            break
        else :
            print('3글자로 입력하세요.')

    return name

def input_birth() :
    while True :
        birth = input('생일과 주민번호뒤1자리(000000-0): ')
        if len(birth) == 8 and birth[6] == '-' and birth[:6].isnumeric() \
            and (birth[7] >= '1' and birth[7] <= '4') :
            break
        else :
            print('형식에 맞지 않습니다. 000000-0 숫자로 입력해주세요.')

    return birth

def go_join(member_info) :
    #회원가입을 처리하는 코드를 작성하세요.


def go_login(member_info) :
    #로그인을 처리하는 코드를 작성하세요.


def go_welcome(member) :
    print('{:*^60}'.format(''))
    print('{:*^60}'.format(' Member Info '))
    print('{:*^60}'.format(''))
    #멤버정보를 화면에 출력하는 코드를 작성하세요.
    
    
    print('{:*^60}'.format(''))

import pickle, sys

def main() :
    
    try : #프로그램 시작 시 Member.dat 파일을 읽어들여 멤버정보를 로드한다.


    except FileNotFoundError :
        member_info = []
    except :
        print('파일 로드 오류, 프로그램을 종료합니다.')
        sys.exit()

    while True :
        print('{:*^60}'.format(''))
        print('{:*^60}'.format(' Welcome '))
        print('{:*^60}'.format(''))

        print('1. Login')
        print('2. Join')
        print('3. exit')

        s = input('메뉴를 선택하세요. : ')
        if s == '1' : #login
            go_login(member_info)
        elif s == '2' : #join
            go_join(member_info)
        elif s == '3' : #exit
            
            try : #프로그램 종료 시 Member.dat 파일에 멤버정보를 저장한다.


            except :
                print('파일 저장 오류, 잠시 후 다시 시도해 주세요.')
            else :
                print('\n종료합니다.\n')
                break
        else :
            print('원하는 메뉴를 입력하세요.')

main()