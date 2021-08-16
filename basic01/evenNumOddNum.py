# 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    answer = ''

    if num%2 == 0:
        answer = 'Even'
        return print(answer)
    else:
        answer = 'Odd'
        return print(answer)

num = 3
# num = 4
# solution(num)


# 다른 사람 풀이1
def solution1(num):
    if num % 2:
        return 'Odd'
    else:
        return 'Even'

# 다른 사람 풀이2
def solution2(num):
    return print(num % 2 and "Odd" or "Even")

solution2(num)

# 다른 사람 코드 리뷰:
# and or 연산에 대해 문법이 부족한 것을 확인
# if 조건식에 True, False값을 쓸 수 있는 것을 알고 있었지만 써먹을 생각을 아예 못함.
# 쉬운 문제였지만 역시나 부족한 내 실력을 확인하게 되는 계기