#파이썬 함수식 및 람다

#함수 정의 방법
#def 함수명(파라미터):
#   code

#함수 호출
#함수명(파라미터)

#함수 선언 위치 중요

#예제1

def hello (world):
    print("Hello", world)

hello ("Python!!")

#예제 2
def hello_return(world):
     val = "Hello " + str(world)
     return val

a = hello_return("python !!!!!")
print(a)

#예제3 (다중 리턴)
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300

    return y1,y2,y3
val1,val2,val3 = func_mul(100)

print(val1,val2,val3)

#예제3 (데이터 타입 반환)
def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300

    return [y1,y2,y3]

lt = func_mul2(100)
print(lt)

# 예제4 
# *args(몇개의 값이있는지 모를때 튜플 형태로 반환), *kwargs

def args_func(*args) :
    # print(args)

    #for t in args :
        #print(t) 가 가능
    for i,v in enumerate(args) :
        print(i,v)
args_func('Kim')  

#kwargs ** dict형태 * 튜플형태
def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

kwargs_func(name1 = 'Kim', name2 ='Park', name3 = 'Lee')

#전체 혼합
def example_mul(arg1, arg2, *args,**kwargs):
    print(arg1,arg2,args,kwargs)

example_mul(10,20,'park','kim',age=24,age2=35)

# 중첩 함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>>',num)
    print("in fuc")
    func_in_func(num +10000)

nested_func(10000)

# 예제 6 힌트 에러가 나진않지만 가독성이 올라감
def func_mul3(x: int)->list:
    y1 = x*100
    y2 = x*200
    y3 = x*300

    return [y1,y2,y3]

print(func_mul3(5))


#람다식(lambda) 예제
#람다식 : 메모리절약 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


#일반적 함수 -> 변수 할당
def mum1_10(num : int)-> int :
    return num*10

var_func = mum1_10
print(var_func)
print(type(var_func))
print(var_func(10))

lambda_mul_10 = lambda num: num*10

print(lambda_mul_10(10))

#함수도 매게 변수 사용가능

def func_final(x,y,func) :
    print(x*y*func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda x : x*1000))
