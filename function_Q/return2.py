# 덧셈
def calc_add(n1, n2):
    result = n1 + n2
    return result

add = calc_add(3,5)
print(add)


# 사각형의 둘레구하기
def square(a,b):
    result = (a+b)*2
    return result

sq = square(3,6)
print(sq)



# 리스트! / 최대값, 최소값 구하기
def maxScore(score_list):
    # max=0
    max = score_list[0]
    for i in score_list:
        if max <= i:
            max = i
    return max

def minScore(score_list):
    min = score_list[0]
    for i in score_list:
        if min >=i:
            min = i
    return min

score = [80,85,91,100,50,75]
maxScore = maxScore(score)
minScore = minScore(score)
print('최고점수는 %d점 입니다' %maxScore)
print('최저점수는 %d점 입니다' %minScore)