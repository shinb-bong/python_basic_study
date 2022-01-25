#Section  04-2 
#문자열,문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'Nice Man'
str3 =''
str4 = str()
print(len(str1),len(str2), len(str3),len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\t Tab\tTab"
print(escape_str2)

#Raw String 
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

#멀티라인

#multi = \
#"""
#문자열
#멀티라인
#테스트 
#"""
#print(multi)

#문자열 연산
str_o1 = '*'
str_02 = 'abc'
str_03 = "def"
print(str_o1*100)
print(str_02+str_03)
str_04 ="Niceman"
print('a' in str_04) # 순회가 가능하다.
print('z' not in str_04)

#문자열 형 변환
# print(str(77)+'a')
# print(str(10.4))

#문자열 함수


# print(a.islower())
# print(b.endswith('e'))
# print(a.replace('nice','good'))
# print(list(reversed(b)))

a ='niceman'
b= 'orange'

print(a[0:3])
print(a[0:len(a)])
print(a[:4]) #처음부터라고 생각
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])