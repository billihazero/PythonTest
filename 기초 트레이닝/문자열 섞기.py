# def solution(str1, str2):
#     result = []
#     for i in range(len(str1)):
#         result.append(str1[i])
#         result.append(str2[i])
#     return ''.join(result)

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer