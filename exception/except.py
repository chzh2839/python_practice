while True:   
    try:
        print("0이 아닌 정수를 입력 : ", end=' ')
        user_num=int(input())
        print(100/user_num)
        break
    except ZeroDivisionError:
        print("0으로 나눌 수 없다.")
    except ValueError:
        print("입력한 값이 정수가 아님.")
    print("프로그램 종료")



