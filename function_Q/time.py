# 1시간 : 3600초, 1분 : 60초

# 초 입력하면 몇시 몇분 몇초인지 

def cal_time(time):
    if time < 24*60*60: #입력한 시간이 24시간이내 인지 확인!
        hour = int(time / (60*60))
        time = time - hour*60*60
        min = int(time /60)
        time = time - min*60
        sec = time
        print('%d시 %d분 %d초 입니다.' %(hour,min,sec))
    else:
        print('입력 시간이 하루를 초과합니다.')

time= int(input("초 입력 : "))
cal_time(time)