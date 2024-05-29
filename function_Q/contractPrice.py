# 통신사 최종요금 구하기
# 사용개월수에 따른 할인금액 : p_dc => 계약금액 * 사용개월수 할인율
# 신용카드 종류에 따른 할인금액 : c_dc => 계약금액 * 신용카드 할인율

def periodDiscount(contractPrice, period):
    if period > 12:
        p_dc = contractPrice * 20/100
    elif period > 6:
        p_dc = contractPrice * 10/100
    else:
        p_dc = contractPrice * 0/100
    return p_dc

def creditcardDiscount(contractPrice, cardcode):
    c_dc = 0
    if cardcode == 13:
        c_dc = contractPrice * 12/100
    elif cardcode == 12:
        c_dc = contractPrice * 8/100
    elif cardcode == 11:
        c_dc = contractPrice * 5/100
    return c_dc


contractPrice = int(input("계약요금 입력 : "))
period = int(input("사용개월수 입력 : "))
cardcode = int(input("신용카드 코드입력 : "))

p_dc = periodDiscount(contractPrice, period)
c_dc = creditcardDiscount(contractPrice, cardcode)

# 최종요금 => 계약금액 - (p_dc + c_dc)
print(contractPrice)
print(p_dc)
print(c_dc)
finalPrice = contractPrice - p_dc - c_dc

print("최종요금은 %d원입니다." %finalPrice)


    
