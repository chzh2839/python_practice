f=open("c:\\python\\test.txt",'r')

while 1:
    line=f.readline()
    if not line:break
    print(line)

f.close()
