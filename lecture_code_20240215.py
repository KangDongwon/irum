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

def go_join() :
    name = input_name()

    try :
        find = False
        with open('Member.txt', 'r') as f :
            for line in f :
                line = f.readline().rstrip('\n').split(',')
                if line[0] == name :
                    find = True
                    break
    except FileNotFoundError :
        pass

    if find == False :
        birth = input_birth()

        age = calculate_age(birth)
        gender = get_gender(birth)
        birthday = get_birthday(birth)

        try :
            with open('Member.txt', 'a') as f :
                f.write(f'{name},{age},{gender},{birthday}\n')
        except :
            print('\n회원가입 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.\n')
        else :
            print(f'\n{name}님 가입되었습니다.\n')
    else :
        print('\n이미 가입된 회원입니다.\n')

def go_login() :
    name = input_name()

    try :
        with open('Member.txt', 'r') as f :
            while True :
                line = f.readline().rstrip('\n').split(',')
                if line[0] == '' :
                    print('\n존재하지 않는 회원입니다.\n')
                    break
                elif line[0] == name :
                    go_welcome(line)
                    break
    except FileNotFoundError :
        print('\n존재하지 않는 회원입니다.\n')

def go_welcome(member) :
    print('{:*^60}'.format(''))
    print('{:*^60}'.format(' Member Info '))
    print('{:*^60}'.format(''))
    print(f'{member[0]}님의 정보')
    print(f'나이 : {member[1]}살')
    print(f'성별 : {member[2]}')
    print(f'생일 : {member[3]}')
    print('{:*^60}'.format(''))


def main() :
    while True :
        print('{:*^60}'.format(''))
        print('{:*^60}'.format(' Welcome '))
        print('{:*^60}'.format(''))

        print('1. Login')
        print('2. Join')
        print('3. exit')

        s = input('메뉴를 선택하세요. : ')
        if s == '1' : #login
            go_login()
        elif s == '2' : #join
            go_join()
        elif s == '3' : #exit
            print('\n종료합니다.\n')
            break
        else :
            print('원하는 메뉴를 입력하세요.')

main()