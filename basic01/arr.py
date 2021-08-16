# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
  
    for i in arr:
        if (answer != []) and (i == answer[-1]):
            continue
            
        else:
            answer.append(i)
    return answer

# arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]

solution(arr)


# 다른 사람 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i] : continue
        a.append(i)
    return a
