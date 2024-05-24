try:
    num1=int(input("피제수를 입력 : "))
    num2=int(input("제수를 입력 : "))
    if num1<=0 or num2<=0:
        raise ArithmeticError("피제수 또는 제수가 0을 입력할 수 없음.")
except ArithmeticError as e:
    print("예외발생 : "+e.args[0])