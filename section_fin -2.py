# 타이핑 게임 제작 및 기본 완성

import random
import time
import winsound # 사운드 출력 필요 모듈
import sqlite3
import datetime

#DB생성 & Auto Commit
#본인 DB경로
conn = sqlite3.connect('C:/python_basic/resource/records.db', isolation_level=None)

#Cursor 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records( id IMTEGER PRIMARY KEY AUTOINCREMEMT, cor_cnt INTEGER , record text, regdate text )")


words =[] #영어 단어 리스트
n = 1 #게임 시도 횟수
cor_cnt = 0 # 정답 개수 

with open('./resource/word.txt', 'r') as f : # with 문은 알아서 close가 됨
    for c in f :
        words.append(c.strip())

print(words) # 단어 리스트 확인

input("Ready? Press Enter Key!") #게임 스타트 // 무조건 String 형태로 들어온다.

start = time.time()

while n <= 5 :
    random.shuffle(words)
    q = random.choice(words)
    
    print()

    print("*문제 # {}".format(n))  # {}사이에 format 안 변수 대입

    print(q)

    x = input() #타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력확인(공백제거)
        print("PASSS")
        #정답 소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else :

        #오답 소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)

        print ("Wrong!")
    n += 1 # 다음 문제 전환

end = time.time() # End Time 기록

et = end - start # 총게임 시간
et = format(et,".3f") # et 를 3번째 소수점 까지 나타내라 라는 format

if cor_cnt>= 3:
    print("합격")
else:
    print ("탈락")


# 기록 DB 삽입

cursor.execute("INSERT INTO records('cor_cnt','records'.'regdate') VALUES(?,?,?)",(cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')))
# 수행 시간 출력

print("게임 시간 : ",et,"초", "정답 개수:{}".format(cor_cnt))

#시작 지점 

if __name__ == '__main__':
    pass



