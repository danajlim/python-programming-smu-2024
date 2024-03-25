# 사용자로부터 파일 이름을 입력받고, 파일 이름의 확장자가 ".png"로 끝나면 ".jpg"로 교체한 후 화면에 출력.
# 확장자가 ".png"가 아니라면, 파일 이름을 있는 그대로 출력

# 파일 이름이 ".png"로 끝나는지 확인
# replace 함수를 사용하지 않고 다른 명령들을 이용해서 문제를 해결할 것

filename=input("파일 이름을 입력하세요")
if filename.endswith(".png"):
    print(filename[:-4]+".jpg")
else:
    print(filename)