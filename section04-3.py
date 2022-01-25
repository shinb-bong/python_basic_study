#Section 04-3 
#리스트,튜플 

#리스트(순서o 중복o 수정o 삭제o)
#선언
a = []
b = list()
c = [1,2,3,4]
d = [10,100,'Pen','Banana','Orange']
e = [10, 100,['Pen','Banana','Orange']]

#인덱싱
print()
#삭제 : del , remove ,pop

#슬라이싱 [뭐부터:뭐전까지]
print(c[1:2])

#튜플(순서o 중복o 수정x 삭제x)
a = ()
b =(1,)
c = (1,2,3,4)
d = (10, 100,('a','b','c'))

print(c[2])
print(d[2][1])

print(d[2:])
print(c+d)
print(c*3)

#튜플함수
 
z = (5, 2,1,3,1)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))