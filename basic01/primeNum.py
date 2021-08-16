# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 0:
            answer += 1
    return answer




# n = 10
# # n = 5
# print(solution(n))





