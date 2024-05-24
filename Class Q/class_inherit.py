## 오버라이딩 : 상속 시, 부모클래스 메서드를 자식클래스에서 재정의!

class Car2:
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재속도(슈퍼클래스) : %d" %self.speed)


class Sedan(Car2):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("현재속도(서브클래스) : %d" %self.speed)
# 서브클래스Sedan에서 upSpeed()메서드 재정의


class Truck(Car2):
    pass
# 아무런 내용이 없어 슈퍼클래스Car2의 메서드를 그대로 상속


class Sonata(Sedan):
    pass


## 변수 선언 부분 ##
s1, t1 = None, None
sonata1 = None


## 메인 코드 부분 ##
s1 = Sedan()
t1 = Truck()
sonata1 = Sonata()

print("승용차 --> ", end="")
s1.upSpeed(200)

print("트럭 --> ", end="")
t1.upSpeed(200)

print("소나타 --> ", end="")
sonata1.upSpeed(200)
