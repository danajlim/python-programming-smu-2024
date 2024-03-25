# 커피 원두 100g의 가격 10000원
# 커피 원두는 200그램부터 100그램 단위로 구매
# 200,300,400그램을 구매할때의 가격을 출력

# 변수에 가격을 저장 후 복합 연산을 통해 단가를 차례대로 더해서 출력

coffee100gprice=10000
coffeeprice=coffee100gprice
coffeeprice+=coffee100gprice

print("커피 원두 200g 가격:", coffeeprice)
coffeeprice+=coffee100gprice

print("커피 원두 300g 가격:",coffeeprice)
coffeeprice+=coffee100gprice

print("커피 원두 400g 가격:", coffeeprice)
