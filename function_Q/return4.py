# 운임비 검색

def fee(city):
    if city == '춘천':
        price = 5000
    elif city == '부산':
        price = 30000
    elif city == '대구':
        price = 20000
    elif city == '수원':
        price = 10000
    else: price = 7700
    return price

city = str(input("가려는 도시명 : "))
price = fee(city)
print('%s까지의 금액은 %d원입니다.' %(city, price))
