# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = -1
    x = n**(1/2)
    
    if (x-int(x) == 0) and (x > 0):
        answer = int((x+1)**2)
        return print(answer)
    else:
        return print(answer)


# n = 121
n = 3
# solution(n)


# 다른 사람 풀이1
def solution1(n):
    import math
    num = math.sqrt(n)

    if math.sqrt(n) == int(math.sqrt(n)) :
        return pow(num+1, 2)

    return -1


# 다른 사람 풀이2
def solution2(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) **2
    return -1

# print(solution2(n))

# 다른 사람 풀이3
import math

def solution3(n):
    x = math.sqrt(n)
    if x % 1 == 0:
        answer = (x+1)**2
    else:
        answer = -1
    return answer



# 다른 사람 풀이 리뷰:
# 알고리즘은 라이브러리를 import하지 않고 푸는 문제인 줄 알았다. 
# 그동안 왜 라이브러리를 쓰면 안된다고 생각했을까.. 고생했던 내 자신이 넘나 한탄스럽,,
# 나눗셈은 항상 실수형으로 떨어지길래 정수값인지 아닌지 어떻게 판별해야할 지 감이 안왔다.
# 나중에 리뷰보고 % 1을 쓰면 되는 엄청 간단한 풀이가 있음을 깨닫고 우둔한 내 머리를 탓했다.
# 그리고 pow()함수라는 게 있음을 처음 알았다. 역시 파이썬 문법 마스터는 갈 길이 멀다
