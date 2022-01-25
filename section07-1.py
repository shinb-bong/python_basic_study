#파이썬 클래스 상세 이해
#Self 클래스 인스턴스 변수

#클래스 , 인스턴스 차이 중요
# 네임 스페이스 : 객체를 인스턴스화 할때 저장된 공간
#클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
#인스턴스 변수 : 객체마다 별도로 존재

#선언

# class 클래스명 :
#     함수
#     함수
#     함수


#예제 1

class UserInfo:
    #속성,메소드
    def __init__(self,name):
        self.name = name
    def user_info_p(self):
        print("Name:", self.name)
        
#namespace
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)

#예제 2
#self의 이해
class SelfTest():   
    def function1() : #클래스 메소드인거임 변수에서 호출을 하면안되고 클래스에서 호출해야함
        print('함수1')
    def function2(self): #인스턴스 메소드
        print('함수2')

self_test = SelfTest()
SelfTest.function1()
self_test.function2()
SelfTest.function2(self_test)

#예제3 
#클래스 변수와 인스턴스 변수

class WareHouse :
    #클래스 변수
    stock_num =0
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num +=1
    
    def __del__(self):
        WareHouse.stock_num -=1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee') #클래스 네임스페이스 , 클래스 변수(공유)

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.stock_num) #클래스 변수는 인스턴스 변수 모두 공유함
print(user2.stock_num)

del user1 #__del__ 함수 작동

print(user2.stock_num)
print(user3.stock_num)


