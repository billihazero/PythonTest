# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5

str, n = input().strip().split(' ')
n = int(n)
if 1<=len(str)<=10 and 1<= n <=5 :
    print(str * n)

else:
    print("다시 입력하세요")