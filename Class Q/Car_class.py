## 클래스 선언 부분 ## (객체 = 속성 + 메서드)
class Car:
    color = ""
    speed = 0

# 해당 클래스의 필드를 인지시키기 위해 'self'라 명기해야 함!
# 'self'는 클래스 안의 메서드임!
    def upSpeed(self, value):
        print('스피드업', value)
        self.speed += value
        if value >= 150:
            self.speed = 150    # 속도 150으로 최대값 설정!

    def downSpeed(self, value):
        self.speed -= value



## 메인 코드 부분 ##

# 1.코드생성 (자동차 3대의 '인스턴스' 구현 : 객체 구조와 똑같이 만들어진 '실체')
myCar1 = Car() # Car() : 생성자 메서드 : 클래스명으로 생성된 메서드
myCar2 = Car()
myCar3 = Car()
# 자바에서는 : Car myCar1 = new Car()

# 2.필드에 값 대입
myCar1.color = "빨강"
myCar1.speed = 0
myCar2.color = "파랑"
myCar2.speed = 0
myCar3.color = "노랑"
myCar3.speed = 0

# 3.메서드 호출하고 출력!
myCar1.upSpeed(30)
print("자동차1의 색상은 %s이고, 현재 속도는 %d이다." %(myCar1.color, myCar1.speed))

myCar2.downSpeed(60)
print("자동차2의 색상은 %s이고, 현재 속도는 %d이다." %(myCar2.color, myCar2.speed))

myCar3.upSpeed(200)
print("자동차3의 색상은 %s이고, 현재 속도는 %d이다." %(myCar3.color, myCar3.speed))

