# K번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = None
    for command in commands:
        print(command)
        i = command[0] 
        j = command[1]
        k = command[2]
        print(i, j, k)
        answer = sorted(array[i:j+1]) 
        print(sorted(array[i:j+1])[k-1])
    



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))