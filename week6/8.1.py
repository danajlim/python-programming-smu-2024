# 사용자로부터 숫자 5개를 입력받고, 가장 큰 값을 찾아서 반환하는 함수
# 이 함수를 활용해서 가장 큰 입력값을 화면에 출력하는 프로그램

# 사용자가 입력하는 숫자 5개는 모두 0보다 큰 양수로 가정
# 자료의 정렬 알고리즘이 적용된 함수를 사용하지 않음

print("5개 정수를 입력하면 가장 큰 값을 화면에 출력합니다.")
max=0
count=0
while count<5:
    n=int(input("숫자 5개를 입력하세요: "))
    if n>max:
        max=n
    count+=1
print(f"최대값은 {max}입니다")
