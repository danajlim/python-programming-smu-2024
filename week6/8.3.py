# 정수의 약수들을 화면에 출력하는 프로그램을 작성
# 12와 16의 약수들을 출력할것

# 정수를 한 개 인자로 전달받고, 약수를 화면에 모두 출력하는 함수

def Divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
print("12의 약수")
Divisors(12)
print("\n16의 약수")
Divisors(16)
