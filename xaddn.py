# x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954#qna

def solution(x, n):
    answer = []

    for i in range(n-1):
        if answer == []:
            answer.append(x)
        d = answer[-1] + x
        answer.append(d)
    return print(answer)

# solution(2, 5)
# solution(4, 3)
solution(-4, 2)


# 다른 사람 풀이1
def solution1(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
        return answer

def solution2(x, n):
    return [x*i for i in range(1, n+1)]

def solution3(x, n):
    return [i*x + x for i in range(n)]