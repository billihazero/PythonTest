# #자료구조 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))



#Quiz
from random import *
users = range(1,21)
print(type(users))

users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중 1명 치킨 3명 커피

print("----당첨자 발표----")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("----축하합니다----")