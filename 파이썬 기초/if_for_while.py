# weather = input("오늘 날씨 ?")
# if weather == "비" or weather == "눈":
#     print("우산챙겨")
# elif weather == "미세먼지":
#     print("마스크 껴")
# else:
#     print("당장나가")

# temp = int(input("기온은 어뗘?"))
# if 30 <= temp:
#     print("더움")
# elif 10 <= temp and temp <= 30:
#     print("ㄱㅊㄱㅊ")
# elif 0 <= temp and temp <= 10:
#     print("추어")
# else :
#     print("나가지마")

# for문
# print('대기번호 : 1')

# for waiting_list in range(5):
#    print("대기번호 : {0}".format(waiting_list))

# starbucks = ["아이언맨", "토르", "위도우"]
# for customer in starbucks:
#    print("{0}, 커피 나왔슴다.".format(customer))

# customer = "앤트맨"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피 끝")

customer = "아이언맨"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름 무엇?")