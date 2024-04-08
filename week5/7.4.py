# 인자로 정수 한 개(매개변수 이름은 n)을 입력 받고, 1부터 n까지의 합을 구해서 반환하는 함수

# 인자로 전달되는 n은 1이상의 정수

def Sum(n):
    if n==1:
        return 1
    return n+Sum(n-1)
    
print(Sum(1))
print(Sum(10))
print(Sum(100))