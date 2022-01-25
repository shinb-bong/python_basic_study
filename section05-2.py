#파이썬 흐름제어(반복문)
#반복문 실습

#기본 반복문 : for while

v1 = 1
while v1 <11 :
    print("v1 is :", v1 )
    v1 += 1

for v2 in range(10): 
    print("v2 is : ",v2)

for v3 in range(1,11) :
    print("v3 is :", v3)

# 1~100합
sum1 = 0
cnt1 = 1
while cnt1 <= 100 :
    sum1 += cnt1 
    cnt1 += 1 

print('1~100:',sum1)
print('1~100 : ',sum(range(1,101))) #range (뭐부터, 뭐미만까지, 몇개씩 건너뛸지)
print("1~100 : ", sum(range(1,101,2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플 , 집합, 사전
# iterable : range , reversed, enumerate, filter, map ,zip

names = ["Kim", "Park","Cho"]

for name in names :
    print (name)

# 사전 키본값은 키 dic.values() 해줘야 값이 들어가고 dic.items() 해야 둘다
#for - else 구문(반복문이 정상적으로 수행된경우 else 블럭 실행)
# break
numbers = [14,3,4,7,10,24,17]

#continue 아래 조건 실행안하고 for문으로 돌아감
lt = ["1", 2,5,True,4.3,complex(4)]
for v in lt :
    if type(v) is float :
        continue
    print("타입 :",type(v))

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A","b","c","D","e","F","G","h"]

for v in q5 :
    if v.isupper():
        continue
    else :
        print(v, end =' ')

print()
# 리스트 컴프리헨션

numbers =[]
#일반적인 방법
for n in range(1,101) :
    numbers.append(n)

print(numbers)


#리스트 컴프리헨션
numbers2 = [x for x in range(1,101)]
print(numbers2)


q3 =["갑","정","병","을"]

q5 = [x for x in q3 if x != "정"]
print(q5)

q6 = [ x for x in range(1,101) if x%2 !=0]
print(q6)