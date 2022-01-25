#파이썬 클래스 상세 이해
# 상속, 다중상속

#예제 1 
#상속 기본
#슈퍼클래스(부모) 및 서브클래스(자식)--> 모든 속성, 메소드 사용 가능

# 라면-> 속성(종류, 회사,맛,면종류, 이름) : 부모 

class Car :
    """ Parent Class"""
    def __init__(self,tp,color) :
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class Show'

class BmwCar(Car):
    """Subclass"""
    def __init__(self, car_name,tp,color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None :
        return "Your car Name : %s" %self.car_name

class BenzCar(Car):
    """Subclass"""
    def __init__(self, car_name,tp,color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None :
        return "Your car Name : %s" %self.car_name        

#일반 사용

model1 = BmwCar('520d')

#상속 정보

print(BmwCar.mro())