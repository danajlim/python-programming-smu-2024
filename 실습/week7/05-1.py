# 컴퓨터는 무작위 숫자 발생기를 이용해서 주사위를 던지는것과 같은 효과를 내도록 함
# 사람은 원하는 숫자를 입력
# 두개를 비교해서 누가 이겼는지 화면에 출력
# 사람이 입력한 숫자가 1-6 사이가 아니면 오류 출력

import random

num1=int(input("숫자를 입력하세요: "))
num2=random.randint(1,6)
if num1 not in range (1,7):
    print("유효한 수가 아닙니다.")
else:
    if num1>num2:
        print("이겼습니다.")
    elif num1<num2:
        print("졌습니다.")
    else:
        print("비겼습니다.")