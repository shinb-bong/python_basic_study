#파이썬 모듈과 패키지

#패키지 예제
#상대 경로 :
# .. : 부모디렉터리
# . : 현재 디렉토리
from pkg.fibonacci import fibonacci as f


#단위 실행 (독립적으로 파일 실행)하는 코드

if __name__ == "main" :
    prt1()
    prt2()