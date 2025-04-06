# a^3이 100을 넘기는 가장 작은 정수
# n1n2+n2n1==110



for n1 in range(1,10):
    for n2 in range(1,10):
        if n1*10+n2+n2*10+n1==110:
            print(f"n1: {n1}, n2: {n2}")
            break
