#사용자로부터 월(month)을 영어 단어로 입력 받고 해당 월이 몇 일까지 있는지 화면에 출력하는 프로그램을 작성하라

# 월의 이름은 첫 글자만 대문자로 쓰도록 함
# 월 이름은 대문자와 소문자를 구별함 (예: January, February)
# 단 월은 1-4월까지만 처리함
# 윤년은 계산하지 않음 (2월은 무조건 28일)
# 1-4월과 다른 달이 입력되면 아무것도 하지 않음

month=input("월을 입력하세요 (첫글자를 대문자로 써주세요): ")

if month=="Feburary":
    print("28일까지 있습니다.")
elif month=="January" and month=="March":
    print("31일까지 있습니다.")
elif month=="April":
    print("30일까지 있습니다.")
