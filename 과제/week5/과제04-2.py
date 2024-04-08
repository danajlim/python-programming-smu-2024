def getNextPeriodPos(txt,startPos):
# txt로 주어진 문자열의 startPos 인덱스부터 시작해서 다음 마침표('.') 위치를 찾아서 인덱스 반환
    if '.' in txt:
        period_pos=txt.find('.',startPos)
        return period_pos
    else : # 마침표가 없다면-1 반환
        return -1

def getNextLine(txt,startPos):
# txt의 startPos부터 다음 마침표(또는 문자열의 끝)까지의 문자열을 반환 (마침표 포함)
    if startPos>=len(txt): # startPos 값이 txt의 길이보다 크거나 같다면 None 반환
        return None
    period_pos=getNextPeriodPos(txt,startPos)
    if period_pos==-1:
        return txt[startPos:]
    else:
        return txt[startPos:period_pos+1]

def main():
#getNextPeriodPos() 함수를 이용해서 마침표의 위치를 모두 출력
# getNextPeriodPos() 함수의 결과가 -1이 나올 때까지 출력
# getNextLine()을 이용해서 마침표까지 문자열을 출력
# 문자열이 끝날 때까지 지속적으로 다음 마침표까지 문자열 출력
    txt="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate,pharetra sapian vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, maleesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."
    start_pos=0
    while True:
        period_pos=getNextPeriodPos(txt,start_pos)
        if period_pos==-1:
            break
        next_line=getNextLine(txt,start_pos)
        print(period_pos)
        print(next_line)
        start_pos=period_pos+1


main()