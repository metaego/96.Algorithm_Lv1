# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
  
    p = 0
    y = 0

    for i in s.lower():
        if i == 'p' :
            p += 1
                   
        elif i == 'y' :
            y += 1
        else:
            continue

    if p == y:
        answer = True  
        return answer

    else:
        answer = False
        return answer


s = 'Hello Python'
solution(s)

# 다른 사람 풀이 1
def solution1(s):
    answer = True

    p = 0
    y = 0

    for i in s:
        if (i == "p" or i == "P") :
            p += 1

        elif (i == "y" or i == "Y"):
            y += 1

    if (p != y):
        answer = False



# 다른 사람 풀이 2
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')