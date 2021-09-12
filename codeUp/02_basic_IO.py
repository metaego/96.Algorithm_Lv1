'''
문자(character)는
0~9, a~z, A~Z, !, @, #, {, [, <, ... 과 같이 
길이가 1인 기호라고 할 수 있다.

변수에 문자 1개를 저장한 후
변수에 저장되어 있는 문자를 그대로 출력해보자.

예시
c = input()
print(c)

와 같은 형태로 가능하다.
'''
# v = input()
# print(v)

'''
변수에 정수값 할당 후 정수값 출력
'''
# v = int(input())
# print(v)

'''
숫자(0~9)와 소수점(.)을 사용해 표현한 수를 실수(real number)라고 한다.

변수에 실수값을 저장한 후
변수에 저장되어 있는 값을 그대로 출력해보자.

예시
f = input()
f = float(f)
print(f)
와 같은 형태로 가능하다.
'''
# f = float(input())
# print(f)

'''
줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

예시
a = input() 
b = input()
print(a)
print(b)
과 같은 방법으로 가능하다.
'''
# a = int(input())
# b = int(input())
# print(b)
# print(a)

'''
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

예시
...
print(f)  #f에 저장되어있는 값을 출력하고 줄을 바꾼다.
print(f)
print(f)
와 같은 방법으로 3번 줄을 바꿔 출력할 수 있다.
'''
# r = float(input())
# print(r)
# print(r)
# print(r)
'''
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

예시
a, b = input().split()
print(a)
print(b)
과 같은 방법으로 두 정수를 입력받아 출력할 수 있다.
'''
# a, b = input().split()
# print(int(a))
# print(int(b))
'''
공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

참고
...
print(c2, c1)와 같은 방법으로 출력하면, 
c1과 c2에 저장된 값이 공백을 두고 순서가 바뀌어 한 줄로 출력된다.
print( ) 안에서 쉼표(,)를 찍어 순서대로 나열하면, 
그 순서대로 공백을 두고 출력된다.
'''
# a, b = input().split()
# print(b, a)
'''
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 
한 줄로 3번 출력해보자.

예시
s = input()
print(s, s, s)  #공백으로 구분해 한 줄로 출력한다.
와 같은 방법으로 3번 출력할 수 있다.
'''
# v = input()
# print(v, v, v)
'''
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

예시
a, b = input().split(':')
print(a, b, sep=':')
와 같은 방법으로 가능하다.
'''
# a, b = input().split(':')
# print(a, b, sep=':')
'''
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
'''
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

'''

주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 
오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.
'''
# n1, n2 = input().split('-')
# print(n1,n2,sep='')
'''
알파벳과 숫자로 이루어진 단어 1개가 입력된다.
입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

예시
s = input()
print(s[0])
print(s[1])
'''
# v = input()
# print(v[0])
# print(v[1])
# print(v[2])
# print(v[3])
# print(v[4])
'''
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

참고
s = input()
print(s[0:2])
'''
# v = input()
# print(v[0:2], v[2:4], v[4:7])

'''
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
'''
# h, m, s = input().split(':')
# print(m)
'''
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

예시
w1, w2 = input().split()
s = w1 + w2
print(s)

참고
단어는 문자(character)들로 만든다.
문자들로 구성된 문장을 문자열(string)이라고 부른다.
문자열에는 공백문자(' ')가 포함될 수 있는데, 
문자 1개는 길이가 1인 문자열이라고 할 수 있고, 
공백문자(' ')가 없는 문자열은 단어(word)라고 할 수 있다.

일반적인 문장들은 공백으로 구분된 단어들로 만들어지기 때문에,
공백문자로 구분된 문장에서 단어를 잘라내기 위해서는 
공백문자(' ')를 기준으로 자르면 된다.
키보드로 입력되는 것들은 기본적으로 문자열로 인식되고, 
문자열끼리 더하기(+)를 실행하면,
두 문자열을 합쳐 연결한(concatenate) 결과를 만들어 낸다.
'''

# s = w1 + w2
# print(s)
w1, w2 = input().split()
print(w1, w2,sep='')