# 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919


def solution(seoul):
    answer = ''
    answer = '김서방은 ' + str(seoul.index('Kim')) + '에 있다'
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))