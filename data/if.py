num=int(input("정수입력:"))
if num%3 == 0 and num%5 == 0:
    result = "3과 5의 배수이다."
elif num%3 == 0:
    result="3의배수"
elif num%5 == 0:
    result="5의배수"
else:
    result = "3과 5의 배수가 아니다."
  
print("%d ==> %s" %(num,result))  
