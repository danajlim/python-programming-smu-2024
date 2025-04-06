clientclass=input("회원등급을 입력하세요: ")
clientmin=int (input("주차 시간(분)을 입력하세요: "))

if clientclass=="플래티넘"or"골드":
    print(f"주차 요금은 {(clientmin-120)/10*1000}원 입니다")
elif clientclass=="실버"or"프렌즈":
    clientbuy=int(input("구매 금액(원)을 입력하세요: "))
    if 30000>clientbuy>=10000:
        print(f"주차 요금은 {(clientmin-60)/10*1000}원 입니다")
    elif clientbuy>=30000:
        print(f"주차 요금은 {(clientmin-120)/10*1000}원 입니다")
else:
    clientbuy=int(input("구매 금액(원)을 입력하세요: "))
    if 50000>clientbuy>=10000:
        print(f"주차 요금은 {(clientmin-60)/10*1000}원 입니다")
    elif clientbuy>=50000:
        print(f"주차 요금은 {(clientmin-120)/10*1000}원 입니다")


########교수님 답#######

membership=input("회원 등급을 입력하세요: ") #회원 등급 입력
parkingTime=int(input("주차 시간을 입력하세요: ")) #주차 시간 분으로 입력

# 회원 등급 확인
if membership=="플래티넘" or membership=="골드": #회원 등급이 플래티넘/골드 
    parkingTime-=120 #주차 시간 -120분

if membership=="실버" or membership=="프렌즈": #회원 등급이 실버/프렌즈
    purchased=int(input("구매 금액을 입력하세요: ")) #구매 금액 입력
    if purchased>=30000: #구매 금액>=30000 - 주차 시간 -=120
        parkingTime-=120
    elif purchased>=10000: #구매 금액>=10000 - 주차 시간 -=60
        parkingTime-=60

if membership=="비회원": # 회원 등급이 비회원
    purchased=int(input("구매 금액을 입력하세요: ")) #구매 금액 입력
    if purchased>=50000: #구매 금액>=50000 - 주차 시간-=120
        parkingTime-=120
    elif purchased>=30000: #구매 금액>=30000 - 주차 시간-=60
        parkingTime-=60

if parkingTime<0: #주차 시간<0이면 주차 시간=0으로 만들어주기
    parkingTime=0

parkingFee=parkingTime//10*1000 #주차 요금 계산

print(f"주차 요금은: {parkingFee}")