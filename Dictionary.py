cabinet = {3: "유재석", 100: "조세호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))
print("hi")

#유무 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"조세호"}
print(cabinet["A-3"])

#새 손님
cabinet["C-50"]  = "하하"
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)

#떠난 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key-value 쌍으로 출력
print(cabinet.items())

#모두 삭제
cabinet.clear()
print(cabinet)