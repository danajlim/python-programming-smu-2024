#정수 한개를 함수의 매개 변수를 통해 입력 받고, 윤년인지 확인해서 True 또는 False를 반환하는 함수를 구현하고 이를 검수하는 프로그램

#윤년의 조건 : 연도가 4로 나누어지면 윤년, 연도가 4로 나누어지면서 100으로 나누어지면 윤년 아님, 연도가 400으로 나누어지면 윤년

# 함수에 전달되는 정수는 0보다 큰 양수로 가정

def isLeapYear(year):
    return (year%400==0) or (year%4==0) and (year%100!=0)


print(isLeapYear(1234))
print(isLeapYear(1900))
print(isLeapYear(2000))
print(isLeapYear(2204))
