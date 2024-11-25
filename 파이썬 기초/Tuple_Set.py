# name = "호랭이"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("호랭이", 20, "코딩")
print(name) 

#집합 (set)
#중복안됨, 순서없음

my_set = {1,2,3,3,3}
print(my_set) #1,2,3 

java = {"유재석", "조세호", "하하"}
python = set(["유재석", "호랭이"])

# java 와 python 모두 할 수 있는 사람
print(java & python)
print(java.intersection(python))

#합집합(java 하거나 python 하거나)
print(java | python)
print(java.union(python))

#차집합(java만 할 수 있는 사람)
print(java - python)
print(java.difference(python))

#파이썬 할 줄 아는 사람 늘어남
python.add("노랭이")
print(python)

#자바 잊어버림
java.remove("하하")
print(java)