# 조건/선택 실행구조
'''
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

예시
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
  print(a)

if b%2==0 :
  print(b) 

if c%2==0 :
  print(c) 

참고 
if 조건식 :
  실행1  #조건식의 평가값이 True 인 경우 실행시킬 명령을 들여쓰기를 이용해 순서대로 작성한다.
  실행2
실행3  #들여쓰기를 하지 않은 부분은 조건식에 상관이 없음 

python 에서는 논리적 실행단위인 코드블록(code block)을 표현하기 위해 들여쓰기를 사용한다.
들여쓰기 방법은 탭(tab), 공백(space) 4개 등 여러 가지 방법을 사용할 수 있지만
한 소스코드 내에서 들여쓰기 길이와 방법은 똑같아야 한다.

a%2==0 은 (a%2)가 먼저 계산된 후 그 결과를 정수 0과 비교한 결과값이다.
a를 2로 나눈 나머지가 0, 즉 짝수이면 True 가 되고, 아니면 False 로 계산된다.
따라서,
if a%2==0 : #a가 짝수라면 ... 
와 같은 의미가 된다. 짝수가 아니라면 들여쓰기로 작성된 부분들은 실행되지 않는다.
'''
# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)
# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)
'''
3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

예시
...
if a%2==0 :
  print("even")
else :
  print("odd") 
...

참고 
if 조건식 :  #조건식을 평가해서...
  실행1      #True 인 경우 실행시킬 명령들...
  실행2
else :        
  실행3      #False 인 경우 실행시킬 명령들...
  실행4
실행5       #조건식과 상관없는 다음 명령
...

else 는 if 없이 혼자 사용되지 않는다.
또한, else 다음에는 조건식이 없는 이유는? True(참)가 아니면 False(거짓)이기 때문에... 
조건식의 평가 결과는 True 아니면 False 로 계산되기 때문이다.

python 에서는 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확하게 해주어야 한다.
'''
# a, b, c = map(int, input().split())

# if a%2==0:
#     print('even')
# else:
#     print('odd')

# if b%2==0:
#     print('even')
# else:
#     print('odd')

# if c%2==0:
#     print('even')
# else:
#     print('odd')
        
'''
0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.

예시
...
if n<0 :
  if n%2==0 :
    print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')
...

참고
조건/선택 실행구조 안에 다시 조건/선택 실행구조를 "중첩"할 수가 있다.

또한, 중첩된 조건은
...
if (n<0) and (n%2==0) :
    print('A')
...
와 같이 논리연산자(not, and, or)를 이용해 합쳐 표현할 수도 있다.
비교연산(<, >, <=, >=, ==, !=) 의 계산 결과는 True 또는 False 의 불(boolean) 값이고,
불 값들 사이의 논리연산(not, and, or)의 결과도 True 또는 False 의 불 값이다.
'''
# a = int(input())
# if a < 0:
#     if a%2 == 0:
#         print('A')
#     else:
#         print('B')
# else:
#     if a%2 == 0:
#         print('C')
#     else:
#         print('D')
'''
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.

예시
...
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D') 
...

참고
여러 조건들을 순서대로 비교하면서 처리하기 위해서 조건문을 여러 번 중첩할 수 있다.

if 조건식1 :
  ...
else :
  if 조건식2 :
    ...
  else :
    if 조건식3 :
      ...
    else :
      ...
...
와 같이 조건/선택 실행 구조를 겹쳐 작성하면 순서대로 조건을 검사할 수 있다.
어떤 조건이 참이면 그 부분의 내용을 실행하고 전체 조건/선택 구조를 빠져나가게 된다.

if 조건식1 : 
  ... 
elif 조건식2 : 
  ... 
elif 조건식3 : 
  ... 
else : 
  ...
도 똑같은 기능을 한다. elif는 else if 의 짧은 약어라고 생각해도 된다.
elif 를 사용하면 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러 번 안 쪽으로 들여쓰기 하지 않아도 된다.
'''
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 70:
#     print('B')
# elif score >= 40:
#     print('C')
# else:
#     print('D')
'''
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''
# eval = input()
# if eval == 'A':
#     print('best!!!')
# elif eval == 'B':
#     print('good!!')
# elif eval == 'C':
#     print('run!')
# elif eval =='D':
#     print('slowly~')
# else:
#     print("what?")
'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

예시
...
if n//3==1 :
  print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.
'''
# month = int(input())
# if month in [12, 1, 2]:
#     print('winter')
# elif month in [3, 4, 5]:
#     print('spring')
# elif month in [6, 7, 8]:
#     print('summer')
# elif month in [9, 10, 11]:
#     print('fall')