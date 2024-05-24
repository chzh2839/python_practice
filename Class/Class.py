# bit : 저장단위의 최소 단위(0,1 로만 표현)
# 1byte  = 8bit
# int : 4byte
# *** Class : 사용자 정의 자료형. 단일변수들이 모인 집합체.
#             String/Int 등과 같이 단일변수로 정의할 수 없음.
# Instance : class에 있는 걸 그대로 구현해내서 만들어낸 객체.
# *** heap 영역 : 사용자 정의 공간.


class Service:
    secret = '영구는 배꼽이 두개다.'
    product = 'Internet'
    def setname(self, name):
        self.name = name # 오른쪽name은 setname함수에서 온 것. 왼쪽name은 클래스에서 온 것. 왼쪽name은 이름 바꿔도 됨.
    def sum(self, a, b): # self : 클래스 안에 있는 함수라는 의미. (자바에서 this)
        result = a+b
        print('%s님, %s + %s = %s입니다.' %(self.name, a,b,result))

yang = Service() # yang => 결과값을 받을 instance
print(yang.secret)
print(yang.product)
# 클래스 안에 있는 변수에 접근하기 위해서 반드시 instance(객체)를 통해서만!!

# > 이건 Service클래스 안 sum함수에 이미 print가 있으니까 중복으로 쓰지 않음
yang.setname('홍길동')
yang.sum(1,2)




secret='이건 클래스 밖에 있는 변수다.'
print(secret)






