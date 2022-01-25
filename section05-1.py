#파이썬 흐름제어(제어문)
#조건문 실습

#예1
if False :
    print("Yes")
else:
    print("NO")

#관계 연산자
#>,>=.<.<= == !=

# 참 거짓 종류 (True,False)
#참 : "내용",[내용],(내용),1 , True
#거짓 : "",[],(),0 <- 빈문자열, False

city ="aaaa"

if city : 
    print(">>>TRUE")
else : 
    print("FALSE")

# 논리 연산자
# and or not

a = 100
b= 6
c=15
print ('and' , a>b and b>c)
print ('or :  ' ,a>b or b>c)
print('not : ', not a>b)
print (not False)

#산술 관계 논리 연산자
#산술 > 관계 > 논리 순서로 적용
num = 90
#다중조건문
if num >= 90 :
    print("합격")
elif num >= 80 :
    print ("준합격")
else :
    print("꽝")

#중첩 조건문

age = 27

height = 175

if age >= 20 :
    if height >= 170:
        print("A 지망 지원가능")
    elif height >= 160:
        print("B 지망 가능")
    else :
        print("지원가능")
else :
    print("지원불가능")

