#파이썬 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리 : 순서 x 중복 x 수정 ㅇ 삭제 ㅇ
#리스트 : [] 튜플: () 딕셔너리: {}
#Key,Value (Json)
#선언
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 980616}
b = {0:'Hello Python0', 1: 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

#출력
print(a['name'])
print(a.get('name')) #안정적으로 접근가능
print(c['arr'][1:3])

#딕서너리 추가
a['address']= 'seoul'

#keys, values,items
print(list(a.keys()))

temp = list(a.keys())
print(temp [1:3])

print(a.values())

# 집합(sets)(순서x, 중복x)

a =  set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(c)
#형 변환을 통해서 사용
t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))

#추가 제거

s3 = set([7,8,9,10])

s3.add(18)
s3.remove(7)