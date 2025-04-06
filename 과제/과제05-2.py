# 2520은 1~10 사이의 모든 정수로 나눠지는 가장 작은 정수
# 1-20 사이의 모든 정수로 나눠지는 가장 작은 정수는 무엇인지 찾는 프로그램

def find_smallest_multiple():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = 1
    for prime in primes:
        exponent = 1
        while prime ** exponent <= 20:
            exponent += 1
        result *= prime ** (exponent - 1)
    return result

result = find_smallest_multiple()
print("1부터 20까지의 모든 정수로 나눠지는 가장 작은 정수:", result)
