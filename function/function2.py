# 반지름 값에 따라 면적이 다름
# 면적 계산 공식이 반복처리 -> 함수로 정의
# public void calculate_area(double radius){
#   ................
# } >> 다른 일반 언어에서의 함수 구조


# def calculate_area(radius):
#     area=3.14*radius*radius
#     return area

# result=calculate_area(5.2)
# print(result)


def cal_area():
    result=3.14*r*r
    return result

r=float(input("반지름 : ")) # float : 실수형으로 바꿔줌
area=cal_area()
print(area)