

inputLocation = int(input("가고자 하는 층을 입력하세요 : "))
nowLocation = int(input("현재 층을 입력하세요 : "))

if inputLocation == nowLocation:
    print("현재 층 floor입니다.")
elif inputLocation >=1 and inputLocation <=6:
    if inputLocation > nowLocation:
        def goUpfloor(now, target):
            for i in range(1, (target-now)+1):
                print("%d 층에 도착했습니다." %(now+i))
        goUpfloor(nowLocation, inputLocation)
    else:
        def goDownfloor(now, target):
            for i in range(1, (now-target)+1):
                print("%d 층에 도착했습니다." %(now-i))
        goDownfloor(nowLocation, inputLocation)
else:
    print("다른 층(1~6)을 입력해주세요.")

