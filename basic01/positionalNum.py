# 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    n = str(n)

    for i in range(len(n)):
        answer += int(n[i])
    return answer 

# n = 123
n = 987
# solution(n)

# 다른 사람 풀이1
def sum_digit(number):
    return sum([int(i) for i in str(number)])

# 다른 사람 풀이2
def sum_digit(number):
    return sum(map(int,str(number)))

# 다른 사람 코드 리뷰:
# map에 대한 개념 부족, sum 존재 망각, comprehension 어려움, for문에서 str도 가능함을 다시 깨달음
# 문법에 대한 개념이 아직도 한참 부족하다는 사실 자각.