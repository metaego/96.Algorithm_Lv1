# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    lst = sorted(list(str(n)), reverse=True)
    for i in lst:
        answer.append(int(i))
    return answer


n = 12345
print(solution(n))



# 다른 사람 풀이1
def solution1(n):
    a = []
    s = reversed(str(n))
    for i in s:
        a.append(int(i))
    return a


# 다른 사람 풀이2
def solution2(n):
	return [int(i) for i in str(n)][::-1]


# 다른 사람 풀이3
def solution3(n):
	return list(map(int, reversed(str(n))))


# 다른 사람 코드 리뷰:
# 우선 NonType error가 왜 발생하는지 알았다.
# 리스트는 요소가 하나 추가된 리스트를 return하지 않는다고 한다.
# 무슨 말인지 정확하게 이해하지 못했지만 lst += lst.append(int(i))가 안되는 이유는
# 자기자신을 return이 안된다고 이해했다. 그래서 위 코드가 아닌 lst.append(int(i))로 써야 NoneType error가 발생하지 않는다
# 그리고 reversed()함수에 대해 새로 알게됐다. 해당 내용에 대해 서치했는데 알 듯 하면서도 모르겠다
# 파이썬 마스터의 길은 멀고도 험하구나
# 전공생들 대단쓰,,