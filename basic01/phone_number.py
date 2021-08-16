# 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''

    num = len(phone_number)
    answer = '*'* (num -4)
    answer += phone_number[-4:]
    return answer
    
# phone_number = "01012345678"
phone_number = "01033334444"
print(solution(phone_number))


# 다른 사람 풀이1:
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]


# 다른 사람 코드 리뷰:
# 먼저 인덱스는 리스트에서만 사용할 수 있다고 잠시 착각을 했었다.
# 덕분에 시간 엄청 잡아먹었음.
# 삽질하다가 str타입에 인덱스 써보니 되는 걸 알고 잠시 충격(..)
# 문자열 길이만큼 *를 반환하면 되는데, 인덱스 그 자리에 *를 반환해야한다는 고집스런 생각에
# 혼자서 삽질하다가 타임오버. 이래서 고정관념이 무서운 거다.
# 난 제발 고집 좀 버렸으면 좋겠다. 으휴으휴으휴
# 다른 사람의 깔끔 간결한 코드에 난 여전히 멀었음을 느낀다. 휴,, 도대체 언제쯤 잘하냐,,