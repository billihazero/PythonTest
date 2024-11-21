# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
# 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.

str = input()

#내장함수 swapcase() : 대소문자 변환해주는 파이썬 내장함수
#print(str.swapcase())

#다른 방법
for i in str:
    if i.islower():
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')