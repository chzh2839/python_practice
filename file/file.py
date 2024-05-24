# 파일객체 = open(file,mode)
# mode : 파일을 열 때 사용하는 모드 (w :쓰기모드, r :읽기모드, a :추가모드)

f=open("c:\\python\\test.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" %i
    # print(data)
    f.write(data)
f.close()
