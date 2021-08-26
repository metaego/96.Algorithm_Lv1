# spj: 스페셜 저지. 
# 정답이 여러가지인 문제나 입력 없이 출력만 하는 문제, 테스트 케이스가 하나만 있는 문제 등에 사용

# 세 개의 정수를 입력 받아서 합계와 평균을 출력하시오. 
# (단 평균은 소수 이하를 버리고 정수부분만 출력한다.)
'''
입력 예
10 25 33

출력 예
sum : 68
avg : 22
'''
# num1, num2, num3 = map(int, input().split())
# print("sum : ", num1 + num2+ num3)
# print("avg : ", (num1 + num2+ num3)//3)


print()
print('='*100)
# 정수 2개를 입력받아서 
# 첫 번째 수에는 100을 증가시켜 저장하고 
# 두 번째 수는 10으로 나눈 나머지를 저장한 후 
# 두 수를 차례로 출력하는 프로그램을 작성하시오.
'''
입력 예
20 35

출력 예
120 5
'''
# num1, num2 = map(int, input().split())
# num1 += 100
# num2 %= 10
# print(num1, num2)

print()
print('='*100)
# 한 개의 정수를 입력 받아서 후치증가 연산자를 사용하여 출력한 후 
# 전치 증가 연산자를 사용하여 출력하는 프로그램을 작성하시오.

# num = int(input())

# print(num)
# num += 1
# num +=1
# print(num)



print()
print('='*100)
# 두 개의 정수를 입력받아서  
# 첫 번째수는 후치 증가 연산자를 사용하고 
# 두 번째 수는 전치 감소 연산자를 사용하여 
# 두 수의 곱을 구한 후 
# 각각의 값을 출력하는 프로그램을 작성하시오.

# python 사용자는 두 번째 수를 1감소시키고 두 수의 곱을 구한후 첫 번째 수를 1증가시킨다. 
# 세 수를 출력한다.
'''
입력 예
10 20

출력 예
11 19 190
'''

# num1, num2 = map(int, input().split())

# num1AfterAdd = num1
# num1AfterAdd += 1
# num2 -= 1 # 전치 감소 연산자
# multipNum = num1*num2
# print(num1AfterAdd, num2, num1*num2)



print()
print('='*100)
'''
두 개의 정수를 입력받아서, 
첫 번째 줄에는 두 정수의 값이 같으면 1 아니면 0을 출력하고, 
두 번째 줄에는 같지 않으면 1 같으면 0을 출력하는 프로그램을 작성하시오.
(JAVA는 1이면 true, 0이면 false를 출력한다.)
'''
'''
입력 예
5 5

출력 예
1
0
'''
# num1, num2 = map(int, input().split())

# if num1 == num2:
#     print(1)
# else:
#     print(0)

# if num1 != num2:
#     print(1)
# else:
#     print(0)

    
print()
print('='*100)
'''
두 개의 정수를 입력받아서 다음과 같이 4가지 관계연산자의 결과를 출력하시오.
이때 입력받은 두 정수를 이용하여 출력하시오.
 (JAVA는 1이면 true, 0이면 false를 출력한다.)
'''
'''
입력 예
4 5

출력 예
4 > 5 --- 0
4 < 5 --- 1
4 >= 5 --- 0
4 <= 5 --- 1
'''
# num1, num2 = map(int, input().split())
# print(num1, '>', num2, '---', int(num1 > num2))
# print(num1, '<', num2, '---', int(num1 < num2))
# print(num1, '>=', num2, '---', int(num1 >= num2))
# print(num1, '<=', num2, '---', int(num1 <= num2))

print()
print('='*100)
'''
2개의 정수를 입력 받아서 논리곱과 논리합의 결과를 출력하는 프로그램을 작성하시오.
(수가 0 이 아닌 경우 참으로, 0 인 경우 거짓으로 간주합니다.)

[JAVA]
2개의 정수를 입력 받아서 0이 아니면 참(true), 0이면 거짓(false)으로 처리하고
두 값의 논리곱과 논리합의 결과를 출력하는 프로그램을 작성하시오.

​hint : 정수 a를 입력받은 후 boolean c = (a != 0);을 실행하면 c에 a의 논리값이 저장된다.
'''
'''
입력 예
2 0

출력 예
0 1

[JAVA]
false true
'''
# num1, num2 = map(int, input().split())
# print(int((num1 != 0) and (num2 != 0)), int((num1 != 0) or (num2 != 0)))


print()
print('='*100)
'''
3개의 정수를 입력 받아 첫 번째 수가 가장 크면 1 아니면 0을 출력하고 세 개의 수가 모두 같으면 1 아니면 0을 출력하는 프로그램을 작성하시오.
(JAVA는 1이면 true, 0이면 false를 출력한다.)
'''
'''
입력 예
10 9 9

출력 예
1 0
'''
# num1, num2, num3 = map(int, input().split())
# if (num1 > num2) and (num1 > num3): 
#     print(1)
# else:
#     print(0)

# if (num1 == num2) and (num1 == num3) :
#     print(1)
# else:
#     print(0)



print()
print('='*100)
'''
국어 영어 수학 컴퓨터 과목의 점수를 정수로 입력받아서 
총점과 평균을 구하는 프로그램을 작성하시오. 
(단 평균의 소수점 이하는 버림 한다.)
'''
'''
입력 예
70 95 63 100

출력 예
sum 328
avg 82
'''
# subj1, subj2, subj3, subj4 = map(int, input().split())

# print('sum %d' % (subj1 + subj2 + subj3 +subj4))
# print('avg %d' % ((subj1+subj2+subj3+subj4)//4))

print()
print('='*100)
'''
두 정수를 입력받아서 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
35 10

출력 예
35 / 10 = 3...5
'''
# num1, num2 = map(int, input().split())
# print('%d / %d = %d...%d' %(num1, num2, num1//num2, num1%num2))

print()
print('='*100)
'''
직사각형의 가로와 세로의 길이를 정수형 값으로 입력받은 후 
가로의 길이는 5 증가시키고 세로의 길이는 2배하여 저장한 후 
가로의 길이 세로의 길이 넓이를 차례로 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
20 15

출력예
width = 25
length = 30
area = 750
'''
# width, length = map(int, input().split())
# width += 5
# length *= 2
# print(f'width = {width}') 
# print(f'length = {length}') 
# print(f'area = {width*length}') 



print()
print('='*100)
'''
두 정수를 입력받아 
첫 번째 수는 전치증가연산자를 사용하고 
두 번째 수는 후치감소연산자를 사용하여 출력하고 
바뀐 값을 다시 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
10 15

출력 예
11 15
11 14
'''
# num1, num2 = map(int, input().split())
# num1add = num1
# num1add += 1











print()
print('='*100)
'''
민수와 기영이의 키와 몸무게를 입력받아 
민수가 키도 크고 몸무게도 크면 1 그렇지 않으면 0을 출력하는 프로그램을 작성하시오.
(JAVA는 1 이면 true, 0 이면 false를 출력한다.)
'''
'''
입력 예
150 35
145 35

출력 예
'''
min_heigh, min_weight = map(int, input().split())
ki_heigh, ki_weight = map(int, input().split())

if (min_heigh > ki_heigh) and (min_weight > ki_weight):
    print(1)
else:
    print(0)