# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    num = 0
    for i in list(str(x)):
        num += int(i)
    if x%num == 0:
        return True
    else:
        return False


# x = 10
# x = 12
# x = 11
x = 13
print(solution(x))



# 다른 사람 풀이1
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0



# 다른 사람 코드 리뷰:
# 리스트 변환하는 문제는 보고 또 봐도 왜 생각해내지 못하는지..
# 이해의 영역과 출력의 영역은 별개의 영역이구낭,,
# sum()함수를 생각했지만 정확하게 사용하는 방법을 까먹어서 좀 돌아가는 코드로 작성함
# 다음 번에는 꼭 리스트 변환 문제에서 해당 방법을 꼭 써먹도록 하쟈,,




