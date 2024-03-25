# "Beautiful.Image.png"파일 이름에서 확장자를 제외한 부분을 화면에 출력

#확장자는 파일 이름의 마지막에 ".확장자" 형태로 주어진다고 가정
# 파일 이름에 "."가 두 개 이상 있을 수 있음(최소 한 개는있음)
# 확장자는 몇 글자인지 정해져 있지 않음

filename="Beautiful.Image.png"
idx=filename.rindex('.') #파일 이름과 확장자를 구분하기 위해 '.'의 위치 찾기
print(filename[:idx]) #확장자를 제외한 부분을 추출하여 출력