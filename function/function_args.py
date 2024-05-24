def sum_mul(choice, *args):
    if choice == "sum":
        result=0
        for i in args:
            result += i
    elif choice == "mul":
        result=1
        for i in args:
            result *= i
    return result

result=sum_mul('sum', 10,2,3)
print(result)

result=sum_mul('mul', 2,2,3)
print(result)

