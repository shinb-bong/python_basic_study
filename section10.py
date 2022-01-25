#파이썬 예외처리의 이해

#예외 종류
#문법적으로 에러가없지만 , 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요

#linter : 코드 스타일, 문법체크

#SyntaxError :잘못된 문법

# print('Test)

#NameError : 참조 변수 없음

# ZeroDivisionError : 0 나누기 에러

#IndexError : 인덱스 범위 오버

#예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']
try:
    z = 'Kim' # cho 예외 발생
    x = name.index(z)
    print('{} Found it!{} in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else!')
