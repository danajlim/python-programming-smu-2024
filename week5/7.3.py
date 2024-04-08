# 세 명의 성적을 입력으로 전달받고, 화면에 순서대로 출력하는 함수를 작성하고, 이 함수를 호출

# 일반적으로 성적은 내림차순으로 출력하지만, 가끔씩 반대로 출력하는 경우도 있음
# 매개 변수를 이용해서 결정할 수 있도록 할 것
# 매개변수의 기본값을 내림차순으로 지정

def compareScores(score1,score2,score3,order=True):
    if order:
        if score1>=score2 and score1>=score3:
            if score2>=score3:
                print(score1,score2,score3)
            else:
                print(score1,score3,score2)
        elif score2>=score1 and score2>=score3:
            if score1>=score3:
                print(score2,score1,score3)
            else:
                print(score2,score3,score1)
        else:
            if score1>=score2:
                print(score3,score1,score2)
            else:
                print(score3,score2,score1)

    else:
        if score1<score2 and score1<score3:
            if score2<score3:
                print(score1,score2,score3)
            else:print(score1,score3,score2)
        elif score2<score1 and score2<score3:
            if score1<score3:
                print(score2,score1,score3)
            else:
                print(score2,score3,score1)
        else:
            if score1<score3:
                print(score3,score1,score2)
            else:
                print(score3,score2,score1)

print("내림차순")
compareScores(85,80,90)
print("오름차순")
compareScores(85,80,90,False)