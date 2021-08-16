# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*'*a)


# 다른 사람 코드1
a, b = map(int, input().strip().split(' '))

for i in range(b):            
    for j in range(a):        
        print('*', end='') 
    print()


# 다른 사람 코드2
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)