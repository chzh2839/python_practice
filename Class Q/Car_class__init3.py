## 클래스 변수 : 클래스 안에 공간이 할당된 변수. 여러 인스턴스가 클래스 변수 공간에 함께 사용/공유

class Car:
    name = "" # 인스턴스 변수(필드)
    speed = 0 # 인스턴스 변수(필드)
    count = 0 # 클래스 변수

    def __init__(self):
        self.name = ""
        self.speed = 0
        Car.count += 1 #######

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name


    def getSpeed(self):
        return self.speed
    def setSpeed(self,speed):
        self.speed = speed


car1 = Car()
car1.setName("QQQ")
car1.setSpeed(20)

print("%s의 현재 속도는 %dkm이고, 생산된 자동차는 %d대입니다." %(car1.getName(), car1.getSpeed(), Car.count))


car2 = Car()
car2.setName("AAA")
car2.setSpeed(60)

print("%s의 현재 속도는 %dkm이고, 생산된 자동차는 %d대입니다." %(car2.getName(), car2.getSpeed(), Car.count))
