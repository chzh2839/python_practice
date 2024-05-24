## 추상 메서드 : 사람의 학번/사번처럼 서브클래스는 다르나 그 기능이 같을 때, 슈퍼클래스에 빈 껍질의 메서드만 만들어놓고 pass로 채움. 
# 서브클래스에서 해당 추상메서드를 오버라이딩함.


class SuperClass:
    def method(self):
        pass

class SubClass1(SuperClass):
    def method(self):
        print("SubClass1에서 method()를 오버라이딩함")

class SubClass2(SuperClass):
    pass
    # def method(self):
        # print("SubClass2에서 method()를 오버라이딩함")


sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()
# SubClass2는 method()를 오버라이딩 안해서 결과값 없음.