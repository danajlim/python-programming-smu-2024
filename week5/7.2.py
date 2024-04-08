# 두개 이상의 단어가 있는 문자열을 입력으로 입력받고, 두번째 단어만 추출해서 반환하는 함수를 구현

#함수에 전달되는 문자열은 반드시 두개 이상의 단어로 구성되어 있다고 가정
#단어는 공백 문자, 웹 문자, 줄바꿈 문자 중 한개로 분리됨
# 문자열의 양끝에 공백 문자가 있을 수 있음(제거 후 단어를 추출)

def getSecondWord(s):
    s=s.strip() #문자열 양 끝의 공백 제거
    pos1=s.find(' ') #첫번째 공백 위치 찾기
    pos2=s.find('\t') #첫번째 tab 위치 찾기
    pos3=s.find('\n') #첫번째 다음행 위치 찾기
    p1=max(pos1,pos2,pos3)+1 #가장 큰 위치값 찾아서 다음 문자열 시작 위치 구하기
    s2=s[p1:] #시작 위치부터 끝까지 문자열 추출

    pos1=s2.find(' ') #첫번째 공백 위치 찾기
    pos2=s2.find('\t') #첫번째 tab 위치 찾기
    pos3=s2.find('\n') #첫번째 다음행 위치 찾기
    p2=max(pos1,pos2,pos3)

    if p2==-1:
        p2=len(s) #두번째 단어가 없으면 문자열 끝까지
    else:
        p2+=p1 #두번째 단어의 끝 위치 계산
    return s[p1:p2] #두번째 단어 반환

print(getSecondWord("what a good day"))
