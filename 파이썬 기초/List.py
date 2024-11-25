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
