## return : 출력값이 딱 하나일때 사용!

def list_add(new_num, num_list):
    if new_num is num_list: # in ?!
        print('이미 원소입니다.')
    else:
        num_list = num_list + [new_num,]
        print('원소를 추가하였습니다.')
    
a= [1,3,5]
list_add(a, a)
list_add(1, a)

def dec_food(coin):
    if coin == '앞':
        print('중국요리')
    elif coin == '뒤':
        print('한국요리')
    else:
        print('기타')

dec_food('뒤')


def print_list(num):
    for n in num:
        if n != 0:
            print(n)
        else:
            break

print_list([1,2,3,0]) # 0이 끝에 있어서 결과값 1,2,3
print_list([1,0,2,3]) # 0이 중간에 있으니 결과값 0전까지 1

