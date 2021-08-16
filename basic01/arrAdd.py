# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = [[]]
    row = len(arr1) 
    col = len(arr1[row-1])

    for i in range(row):
        for j in range(col):
            arr1[i][j] += arr2[i][j]
    answer = arr1        
    return answer

arr1 = [[1,2],
        [2,3]]
arr2 = [[3,4],
        [5,6]]

# arr1 = [[1],
#         [2]]
# arr2 = [[3],
#         [4]]

solution(arr1, arr2)

 # 시간 많이 걸린 이유
 # : return의 줄 맞춤을 잘못해서 for문 도는 동안 반복해서 돌았다.
 # 그런데 그 이유를 한참동안이나 몰랐다. 
 # 들여쓰기의 중요성을 다시 깨닫는다.






 # 다른 사람의 코드1
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

# 다른 사람의 코드 2
def sumMatrix(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# 다른 사람의 코드 3
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer



# 다른 사람의 코드 보고 느낀점:
# zip과 list comprehension의 공부가 부족함을 느낀다.
