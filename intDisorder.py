# 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    lst = list(str(n))
    lst.sort(reverse = True)
    answer = int(''.join(lst))
    return answer


n = 118372
print(solution(n))



# 다른 사람 풀이1
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))


# 다른 사람 풀이2
def solution(n):
    return int("".join(sorted(list(str(n)), reverse = True)))


# 다른 사람 코드 리뷰:
# join함수의 존재를 잊어버렸다.
# int타입을 list에 집어넣는 것을 못해서 한참을 헤맸다. 
# for문을 사용하면 되지 않을까 했는데 자꾸 none이 나와서 왜 none이 나오는지 이해를 못했다.
# sort()만 알았지 sorted()가 있는지 몰랐다. 찾아보니 매개변수 데이터를 새로운 정렬된 리스트로 반환해주는 함수라고 한다
# 이 좋은 걸 왜 나만 몰랐지...
# 파이썬 문법 기초가 부족한 것을 알고리즘 문제 풀면서 절절히 느낀다.