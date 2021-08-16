# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i%divisor == 0:
            answer.append(i)
  
    if answer == []:
        answer.append(-1)
    return sorted(answer)

arr = [5, 9, 7, 10]
# arr = [2, 36, 1, 3]
# arr = [3,2,6]
divisor = 5
# divisor = 1
# divisor = 10
print(solution(arr, divisor))


# 다른 사람 풀이1:
def solution1(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

# 다른 사람 풀이2:
def solution2(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];



# 다른 사람 코드 리뷰:
# 문제를 풀때마다 이건 comprehension으로 풀 수 없지 않을까 생각했다.
# 그런데 항상 풀고 나면 comprehension으로 푼 답안이 보인다
# 볼 때마다 좌절감을 느낀다.
# 이 길은 내 길이 아닌걸까,,,,,,,,,,,,,,,,,,
# 난 언제쯤 문제 푸는 것에서 벗어나 간결한 코드를 작성할 수 있게 될까(엉엉)
# or [-1]의 새로운 사용법을 배웠다. 
# 오늘 배운 거 머릿속에 꼭꼭 집어넣어서 다음번에는 꼭 써먹어야지