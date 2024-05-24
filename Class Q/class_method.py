class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        print(self.length, "길이의 선이 생성되었습니다.")

    def __del__(self):
        print(self.length, "길이의 선이 삭제되었습니다.")

    def __repr__(self):
        return '선의 길이 : ' + str(self.length)
    # 인스턴스를 print문으로 출력할때

    def __add__(self, other):
        print('호호호')
        return self.length + other.length

    def __lt__(self, other):
        print('gkgkgk')
        return self.length < other.length
    # lt, le, gt, ge, eq, ne : 비교연산자 < <= > >= == != 등 사용할때! (인스턴스끼리!)

    def __eq__(self, other):
        return self.length == other.length


## 메인 코드 부분 ##
myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1) ## __repr__()

# print("두 선의 길이 합 : ", myLine1 + myLine2) ## __add__()

if myLine1 < myLine2:
    print('선분2가 더 기네요.')   ## __lt__()
elif myLine1 == myLine2:
    print('두 선분이 같네요.')  ## __eq__()
else:
    print('모르겠네요.')



