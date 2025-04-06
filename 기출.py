def verifyLength(license_plate):
    if len(license_plate)==8 or len(license_plate)==9:
        return True
    else:
        print("veriftLength 오류 : 번호 길이가 너무 길거나 짧음")
        return False

def verifyHangul(license_plate):
    hangulposition=3 or 4
    if license_plate[hangulposition].isalpha() and '가' <= license_plate[hangulposition] <= '힣':
        return True
    else : 
        print("verifyHangul 오류: 한글 위치가 적절치 않음")
        return False

def verifySpace(license_plate):
    spaceposition=4 or 5
    if license_plate[spaceposition]==' ':
        return True
    else: 
        print("verifySpace 오류:공백 문자의 위치가 적절치 않음")
        return False

def verifyLastNum(license_plate):
    last_num=license_plate[-4:]
    if last_num.isdigit():
        last_num_int=int(last_num)
        if last_num_int>=100:
            return True
        else:
            print("verifyLastNum 오류: 뒷 번호가 100 미만임")
            return False
    else:
        print("verifyLastNum 오류: 뒷 번호가 100 미만임")
        return False

def verifyNum3(license_plate):
    first_three_digits = license_plate[:3]
    if first_three_digits.isdigit():
        first_three_int = int(first_three_digits)
        if first_three_int >= 100 and first_three_int <= 999:
            return 1
        else:
            return -1
    else:
        return 0

def verifyNum2(license_plate):
    first_two_digits = license_plate[:2]
    if first_two_digits.isdigit():
        first_two_int = int(first_two_digits)
        if first_two_int >= 1 and first_two_int <= 99:
            return 1
        else:
            return -1
    else:
        return 0

def verifyFirstNum(license_plate):
    result_verifyNum2 = verifyNum2(license_plate)
    result_verifyNum3 = verifyNum3(license_plate)
    if result_verifyNum2 == 1 or result_verifyNum3 == 1:
        return True
    elif result_verifyNum2 == 0 or result_verifyNum3 == 0:
        print("verifyFirstNum 오류: 앞 번호가 숫자가 아님")
        return False
    else:
        return False

def verifyLicensePlate(license_plate):
    if (verifyLength(license_plate) and
        verifyHangul(license_plate) and
        verifySpace(license_plate) and
        verifyLastNum(license_plate) and
        verifyFirstNum(license_plate)):
        return True
    else:
        return False


testdata=[
    "100가 1111",
    "00가 1111",
    "100 가1111",
    "10 가1111",
    "1가  1111",
    "000가 1111",
    "10가111",
    "1001가1111"
]

for data in testdata:
    print(f"자동차 번호: {data},결과 : {verifyLicensePlate(data)}")