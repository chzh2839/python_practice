score=[90,35,89,100,78]
num = 0
for i in score:
    num = num+1
    if i<60: continue
    print("%d번 학생은 합격입니다." %num)
