# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if len(s)%2 == 0:
        answer = s[len(s)//2-1] + s[len(s)//2]  
        # print("if문:", answer)
        return answer
    else:
        answer = s[len(s)//2]
        # print("else문:", answer)
        return answer


s = "abde"
# s = "abcde"
solution(s)


# 다른 사람 코드
def solution1(s) :
    center = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]