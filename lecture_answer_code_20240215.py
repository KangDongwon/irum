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
    #member_info : 리스트, 리스트의 각 값은 딕셔너리
    name = input_name()
    find = False
    for member in member_info :
        if member.get('이름') == name :
            find = True
            break

    if find == False :
        birth = input_birth()

        member = dict()
        member['이름'] = name
        member['나이'] = calculate_age(birth)
        member['성별'] = get_gender(birth)
        member['생일'] = get_birthday(birth)

        member_info.append(member)

        print(f'\n{name}님 가입되었습니다.\n')
    else :
        print('\n이미 가입된 회원입니다.\n')


def go_login(member_info) :
    #로그인을 처리하는 코드를 작성하세요.
    name = input_name()
    find = False
    for member in member_info :
        if member.get('이름') == name :
            find = True
            go_welcome(member)
            break

    if find == False :
        print('\n존재하지 않는 회원입니다.\n')

def go_quit(member_info) :
    name = input_name()
    find = False
    for member in member_info :
        if member.get('이름') == name :
            find = True
            break
    
    if find == True :
        member_info.remove(member)
        print(f'\n{name}님 탈퇴되었습니다.\n')
    else :
        print('\n존재하지 않는 회원입니다.\n')

def go_welcome(member) :
    print('{:*^60}'.format(''))
    print('{:*^60}'.format(' Member Info '))
    print('{:*^60}'.format(''))
    #멤버정보를 화면에 출력하는 코드를 작성하세요.
    print(f'{member.get("이름")}님의 정보')
    print(f'나이 : {member.get("나이")}살')
    print(f'성별 : {member.get("성별")}')
    print(f'생일 : {member.get("생일")}')


    print('{:*^60}'.format(''))

import pickle, sys

def main() :

    try : #프로그램 시작 시 Member.dat 파일을 읽어들여 멤버정보를 로드한다.
        with open('Member.dat', 'rb') as f:
            member_info = pickle.load(f)

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
        print('3. Quit')
        print('4. exit')

        s = input('메뉴를 선택하세요. : ')
        if s == '1' : #login
            go_login(member_info)
        elif s == '2' : #join
            go_join(member_info)
        elif s == '3' : #quit
            go_quit(member_info)
        elif s == '4' : #exit
            try : #프로그램 종료 시 Member.dat 파일에 멤버정보를 저장한다.
                with open('Member.dat', 'wb') as f:
                    pickle.dump(member_info ,f)
            except :
                print('파일 저장 오류, 잠시 후 다시 시도해 주세요.')
            else :
                print('\n종료합니다.\n')
                break
        else :
            print('원하는 메뉴를 입력하세요.')

main()