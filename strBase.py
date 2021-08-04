# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

import re
def solution(s):
    answer = True
    p = re.compile('[a-zA-Z]')
    m = p.findall(s)

    if (len(s) == 4 or len(s) == 6) and (m == []):
        return answer
    else:
        return not answer

s = "a234"
# s = "1234"

solution(s)


# 다른 사람 풀이1
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 다른 사람 풀이2
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))


# 다른 사람 풀이3
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 


# 다른 사람 풀이 리뷰:
# 정규표현식이 익숙치 않아서 문제 풀이에 애를 먹었고 정규표현식을 쓰지 않고 문제 푸는 방법이 있을 것 같았는데
# 다른 사람 풀이3처럼 예외처리를 사용하는 방법은 생각지도 못했다.
# 그리고 isdigit()라는 함수가 있다는 것을 처음 알았다.
# 4 또는 6을 찾는 것을 튜플에 담아 in을 사용하는 것도 생각지도 못했다.
# 쉬운 문제였지만 다른 사람의 코드를 보고 많이 배웠다.
