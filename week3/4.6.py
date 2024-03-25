# 커피 원두 100그램 단가와 무게를 사용자로부터 입력받고 가격 계산해서 화면에 출력

# 커피 원두 단가는 원 단위의 정수로 입력 받기
# 무게는 실수로 입력 받기
# 문자열 출력은 f문자열 사용

coffee100gprice=int (input("커피 원두 100g의 단가를 입력하세요: "))
weight=float(input("구매할 커피 원두의 무게를 입력하세요: "))

print(f"커피 원두 {weight}g 가격: {weight/100*coffee100gprice}")