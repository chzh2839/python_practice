class Car:
    name = ""
    speed = 0

    # name, speed에 값을 저장한다는 개념 (setXXXX와 같은 개념)
    def __init__(self, name, speed):
        self.name = name # 자바 : this.name = name
        self.speed = speed
### 속성/저장 메서드 : setXXXX(매개변수) / 속성(필드값)을 가지고 데이터를 저장하는 메서드
    # def setName(self,name):
    #     self.name = name
    # def setSpeed(self,speed):
    #     self.speed = speed


### 속성에 저장된 값을 읽어옴. : getXXXX(매개변수)
    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


## 변수 선언 부분 ##
# 클래스 : 사용자가 필요에 의해서 만든 객체형 데이터
car1, car2 = None, None #=> 전역변수

## 메인 코드 부분 ##
car1 = Car("아우디",10)
car2 = Car("벤츠",50)

print("%s의 현재 속도는 %d입니다." %(car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." %(car2.getName(), car2.getSpeed()))
