#리스트 list
[1,2,3,"abc"] #요소가 4개인 리스트
[1,2,3,[1,2]] #요소에 리스트 포함됨

#리스트 생성
mylist=[]
mylist=list()

#리스트 요소 추가
a=[]
a.append(4)
a.append('5')
a.append([2,3])

#리스트 요소 개수 확인
e=[]
len(e)

#인덱싱
l=[1,2,3,"abc"]
print(l[0],l[1],l[2],l[3])

#슬라이싱
a=[1,2,3,"abc",4,5]
a[1:3] #2번째부터 3번째까지
a[:3] #[3,"abc"]
a[2:] #[3,"abc",4,5]
a[:] #[1,2,3,"abc",4,5]
a[2:5:2] #[3,4]
a[2::2] #[3,4]

#연결하기
a=[1,2,3]
b=["abc",4,5]
c=a+b #[1,2,3,"abc",4,5]

#반복하기
