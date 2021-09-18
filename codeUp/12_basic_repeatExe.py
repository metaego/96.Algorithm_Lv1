# 반복실행구조
'''
임의의 정수가 줄을 바꿔 계속 입력된다.
-2147483648 ~ +2147483647, 단 개수는 알 수 없다.

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

예시
...
n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)
...

참고
if 조건식 :
  ...
  ...


구조를 사용하면,
주어진 조건식의 평가 결과가 True 인 경우에만, 들여쓰기로 구분된 코드블록이 실행된다.

if 를 while 로 바꾸면?

while 조건식 :
  ...
  ...

와 같은 방법으로 반복해서 실행시킬 수 있다.

실행되는 과정은
1. 조건식을 평가한다.
2. True 인 경우 코드블록을 실행한다.
3. 다시 조건식을 평가한다.
4. True 인 경우 코드블록을 실행한다.
...
... 조건식의 평가 값이 False 인 경우 반복을 중단하고, 그 다음 명령을 실행한다.

조건식의 평가 결과가 True 동안만 반복 실행된다. 

반복실행구조 안에 다른 조건/선택실행구조를 넣을 수도 있고...
조건/선택실행구조 안에 다른 반복실행구조를 넣을 수도 있다.
'''
# n = int(input())
# while n != 0:
#     print(n)
#     n = int(input())
'''
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...
반복 실행구조를 사용해 보자.

예시
...
while n!=0 :
  print(n)
  n = n-1
...

참고
n = n-1  #n에 저장되어있던 값에서 1만큼 뺀 후, 그 값을 다시 n에 저장시킨다.
n -= 1 과 같이 짧게 작성할 수도 있다. n -= 1 은 n = n-1 과 같은 의미이다.
이렇게 산술연산자(+, -, *, / ... )와 대입 연산자(=)를 함께 쓰는 것을 복합대입연산자라고도 부른다.
같은 방법으로 +=, *=, /=, //=, %=, &=, |=, ^=, >>=, <<=, **= 등과 같이 짧게 작성할 수 있다.

처음에 조건식을 검사하고, 그 다음에 실행하고, 그 다음에 값을 바꾸고...
다시 조건식을 검사하고, 실행하고, 값을 바꾸고...
'''
# n = int(input())
# while n != 0 :
#     print(n)
#     n -= 1
'''
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

참고
조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.
'''
# n = int(input())
# while n != 0:
#     print(n-1)
#     n -= 1
'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

예시
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

참고
알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 
즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
(end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.)
'''
# c = ord(input())
# t = ord('a')
# while t <= c:
#     print(chr(t), end = ' ')
#     t += 1

'''
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
'''
# n = int(input())
# c = 0
# while c <= n:
#     print(c)
#     c += 1
'''
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

예시
n = int(input())
for i in range(n+1) :
  print(i)

참고
range(n) 은 0, 1, 2, ... , n-2, n-1 까지의 수열을 의미한다.
예를 들어 range(3) 은 0, 1, 2 인 수열을 의미한다.

for i in range(n) :    
    #range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장해 가면서...
이때의 for는 각각의 값에 대하여... 라는 for each 의 의미를 가진다고 생각할 수 있다.

range(끝)
range(시작, 끝)
range(시작, 끝, 증감)
형태로 수열을 표현할 수 있다. 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)
증감할 수를 작성하지 않으면 +1이 된다.

반복 실행구조에 반복 횟수를 기록/저장하는 변수로 i를 자주 사용하는데,
i 는 반복자(iterator)를 나타내는 i라고 생각할 수 있다. 
i, j, k ... 알파벳 순으로 사용하기도 한다.
'''
n = int(input())
for i in range(n+1):
    print(i)