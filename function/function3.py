def get_sum(start,end):
    sum=0
    for i in range(start,end):
        sum += i
    return sum

print(get_sum(1,101)) # 1~100까지의 합 구하기