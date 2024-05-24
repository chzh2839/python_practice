# according to Class.py 

class Service:
    secret = '영구는 배꼽이 두개다.'
    product = 'Internet'
    
    def __init__(self, name):
        self.name = name
        
    def sum(self, a, b):
        result = a+b
        print('%s님, %s + %s = %s입니다.' %(self.name, a,b,result)) 
        print(self.secret)
        print(self.product)

hong = Service('이순신') # 생성자 함수(객체를 생성 시 초기화시킴 initialization)
hong.sum(1,2)