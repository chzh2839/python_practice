# 제품 가격과 부가세 구하기

def productPrice(totalPrice):
    # p_Price = totalPrice - totalPrice/11
    p_Price = totalPrice*10/11
    return p_Price

def calc_tax(totalPrice):
    tax = totalPrice/11
    return tax


product = int(input("제품가격 : "))
p = productPrice(product)
t = calc_tax(product)
print("제품가격은 %d원, 부가가치세는 %d원입니다." %(p,t))


