coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피량은 %d입니다." %coffee)
    if not coffee:
        print("커피가 떨어짐. 판매중지.")
        break
    
