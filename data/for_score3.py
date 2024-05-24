score=[90,25,67,45,80]

for i in range(len(score)):
    if score[i] < 60 : continue
    print("%d번 학생 합격입니다." %(i+1))
    
