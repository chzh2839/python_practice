class HousePark:
    # 선언(동작적인 부분 없음) : 변수
    # 동작적인 부분 : 함수(명령어들의 모임)
    lastname = '박'
    # def setname(self, name):
    #     self.fullname = self.lastname + name
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, place):
        print('%s씨는 %s여행을 갑니다.' %(self.fullname, place))
    def __del__(self): # 메모리 삭제
        print('%s씨가 사라졌습니다.' %self.fullname)
    

# a=HousePark()
# b=HousePark()
# print(a.lastname)
# print(b.lastname)
# print(HousePark.lastname)

# # c=HousePark()
# # c.setname('사랑')
# print(c.fullname)

# c.travel('미국')

d=HousePark('러브')
d.travel('태국')

f=HousePark('응용')
f.travel('중국')

del d # d랑 f가 같은 클래스 안에 있는 객체기 때문에 다 같이 사라짐.
