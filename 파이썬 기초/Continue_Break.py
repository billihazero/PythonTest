absent = [2, 5]
no_book = [7]
#range() 함수
#정수 시퀀스를 생성하는 함수로 주로 for 루프와 함께 사용되어 반복 작업을 수행한다.
#range(start, stop, stop) 시작값, 종료값, 증감값

for student in range(1, 11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("{0}, 교무실 ㄱㄱ".format(student))
        break
    print("{0}, 책읽어".format(student))