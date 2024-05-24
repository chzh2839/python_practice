## 생성자 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수!
## __init__(self)

class Car:
    color = ""
    speed = 0

    ######### 기본 생성자 ########
    # def __init__(self):
    #     self.color = "빨강"
    #     self.speed = 0

    ######### 매개변수 2개 받는 생성자 ########
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2


    def upSpeed(self, value):
        self.speed += value
        if value >= 150:
            self.speed = 150

    def downSpeed(self, value):
        self.speed -= value



## 메인 코드 부분 ##

# myCar1 = Car()
# myCar2 = Car()
myCar3 = Car("노랑", 60)

# print("자동차1의 색상은 %s이고, 현재 속도는 %d이다." %(myCar1.color, myCar1.speed))
# print("자동차2의 색상은 %s이고, 현재 속도는 %d이다." %(myCar2.color, myCar2.speed))
print("자동차3의 색상은 %s이고, 현재 속도는 %d이다." %(myCar3.color, myCar3.speed))

