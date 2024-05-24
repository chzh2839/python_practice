def cal_area(radius):
    global area # global로 선언하면 지역변수여도 전역변수로 사용가능
    area=3.14*radius*radius
    return # 상식적으로 return area가 맞지만, global area로 선언해서 전역변수로
    
area=0
r=float(input("반지름 : "))
cal_area(r)
print(area)