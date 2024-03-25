# 사용자로부터 주민등록번호를 ******-******* 형태로 입력 받고, 적합한지 아닌지 화면에 출력하는프로그램 작성
# 주민등록번호 적합성 여부 확인 방법
# 전체 글자 수('-' 포함) 및'-'의 위치 확인
# 년도와 월, 일 확인(년도는 0~23년은 2000년대, 24~99까지는 1900년대로 가정)
# 월과 일이 적합한지 확인(2월은 윤년이면 29일까지 아니면 28일까지. 그 밖의 달은 30일인지 31일 이내인지 확인)
# '-' 다음 숫자는 2000년 이후 출생자는 3, 4번으로 시작. 그 이전 출생자는 1, 2번으로 시작하는지 확인


def check(rnumber):
    byear = int(rnumber[0:2])
    bmonth = int(rnumber[2:4])
    bday = int(rnumber[4:6])
    firstnumber = int(rnumber[7])

    leap_year = (byear % 4 == 0 and byear % 100 != 0) or (byear % 400 == 0)

    if not (len(rnumber)==14 and rnumber[6]=="-"):
        return False

    if 0 <= byear <= 23:
        byear += 2000
    elif 24 <= byear <= 99:
        byear += 1900
    else:
        return False

    if firstnumber == 3 or firstnumber == 4:
        if byear>=2000:
            return True
        else:
            return False
    elif firstnumber == 1 or firstnumber == 2:
        if byear>=1900:
            return True
        else:
            return False

    if not (1 <= bmonth <= 12 and 1 <= bday <= 31):
        return False

    if bmonth == 2:
        if leap_year and bday <= 29:
            return True
        elif not leap_year and bday <= 28:
            return True
        else:
            return False
    elif bmonth in [4, 6, 9, 11] and bday <= 30:
        return True
    elif bmonth in [1, 3, 5, 7, 8, 10, 12] and bday <= 31:
        return True
    else:
        return False


rnumber = input("주민등록번호를 입력하세요 (******-*******): ")

if check(rnumber):
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지않습니다.")
