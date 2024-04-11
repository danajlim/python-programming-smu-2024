# 동전을 던져서 앞/뒷면이 나오는 횟수를 세고, 1/2 확률에 수렴하는지 확인하는 프로그램
# random.randint()함수를 사용해서 두개 숫자 중 한개를 무작위로 생성하여 돈전의 앞/뒷면 대신
#100,1000,10000회 던져서 앞/뒷면이 나오는 횟수를 각각 출력

#정해진 횟수만큼 동전을 던지고 앞/뒷면이 나오는 횟수를 출력하는 함수를 구현
#동전을 던지는 횟수는 함수에 입력으로 전달
# 앞/뒷면이 나오는 확률을 구해서 각각 출력

import random
def filpcoin(n):
    Front=0
    Back=0
    for i in range(n):
        if random.randint(0,1)==0:
            Front+=1
        else:
            Back+=1
    print(n, "번 던짐")
    print("앞면이 나올 확률: ",Front/n)
    print("뒷면이 나올 확률: ", Back/n)
    
filpcoin(100)