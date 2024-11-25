#문자열
#파이썬은 라인 단위로 번역해서 실행한다.
sentence = "나는 소년입니다."
print(sentence)
sentence2 = "파이썬은 쉽다"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉽다
"""
print(sentence3)

sentence4 = "나는 소년이고 파이썬은 쉽다"
print(sentence4)

# 슬라이싱
jumin = "990102-1234567"
print("생년월일:", jumin[0:6])

# 7번째 부터 끝까지
print("뒷자리: ", jumin[7:])

#뒤에서 7번째 부터 끝까지
print("뒷자리: ", jumin[-7:])

#2번째 부터, 뒤에서 8번째 까지
print("생일: ", jumin[2:-8])

#문자열 포맷
print ("a" + "b")
print ("a","b")

#방법1
print("나는 %d살 입니다." % 28)
print("나는 %s를 좋아해요." % "과일")

subway = [10, 20, 30]
print(subway)

subway = ["유재석", '박명수', '조세호']
print(subway)

#조세호가 몇번째에 타고 있는가
print(subway.index('조세호'))

#하하가 다음칸에 탄다
subway.append("하하")
print(subway)

#정형돈을 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

#한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)

print(subway.count("유재석"))

# 정렬하기
num_list = [1,5,3,6,2] 
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)


#다양한 자료형 
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
