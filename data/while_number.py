num=0
while num != 4:
    print("1. ADD 2. DEL 3. LIST 4.QUIT")
    num = int(input("번호선택:"))

    if num==1:
        print("자료추가")
    elif num==2:
        print("자료삭제")
    elif num==3:
        print("자료출력")
    elif num==4:
        print("종료")
    

