# 템포, 음량 새로 입력하기

def tempo(now_tempo, num):
    now_tempo += num
    return now_tempo

# now_tempo = 0
# print("현재 템포는 %d입니다." %now_tempo)
# num = int(input("조정 값 입력 : "))
# val = tempo(now_tempo, num)
# print("조정한 후의 템포는 %d입니다." %val)



def volume(vol):
    currV = 3
    currV = currV + vol
    return currV

# currV = 3
# print("현재 음량은 %d입니다." %currV)
# vol = int(input("증가시킬 음량 입력 : "))
# change = volume(vol)
# print("증가 후의 음량은 %d입니다." %change)


# 출근사원체크하기
def work(name):
    member_list = ['이순신', '홍길동', '김춘추','김가네','유관순']
    for member in member_list:
        if member == name:
            return True
    return False

name = str(input("이름입력 : "))
if work(name):
    print("출근완료되었습니다.")
else:
    print("출근불가합니다.")
