# 논리연산
'''
2개의 정수값이 입력될 때,
그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

예시
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

참고
and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 
나머지 경우는 False 로 계산한다.
이러한 논리연산을 AND 연산(boolean AND)이라고도 부르고, · 으로 표시하거나 생략하며, 
집합 기호 ∩(교집합, intersection)로 표시하기도 한다. 
모두 같은 의미이다.

참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 
True 또는 False 의 불 값으로 계산된다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 
True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
'''
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
'''
2개의 정수값이 입력될 때,
그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

참고
or 예약어는 주어진 두 불 값 중에서 하나라도 True 이면 True 로 계산하고, 
나머지 경우는 False 로 계산한다.
이러한 논리연산을 OR 연산(boolean OR)이라고도 부르고, + 로 표시하거나, 
집합 기호 ∪(합집합, union)로 표시하기도 한다.
모두 같은 의미이다.

참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 
True 또는 False 의 불 값으로 계산된다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 
True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
'''
# a, b = input().split()
# print(bool(int(a)) or bool(int(b)))
'''
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

예시
...
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

참고
참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 
XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.

논리연산자는 사칙(+, -, *, /) 연산자와 마찬가지로 여러 번 중복해서 사용할 수 있는데, 
사칙 연산자와 마찬가지로 계산 순서를 표시하기 위해 괄호 ( )를 사용할 수 있다.
괄호를 사용하면 계산 순서를 명확하게 표현할 수 있다.

수학 식에서는 소괄호 (), 중괄호 {}, 대괄호 []를 사용하기도 하지만, 
프로그래밍언어에서는 소괄호 ( ) 만 사용한다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 
True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다
'''
# a, b = input().split()
# print(bool(int(a)) != bool(int(b)))
'''
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
'''
# a, b = input().split()
# print(bool(int(a)) == bool(int(b)))
'''
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
'''
# a, b = input().split()
# print((bool(int(a)) == False) and (bool(int(b)) == False))
# # 다른 사람 풀이 참고1
# a, b = input().split()
# c= bool(int(a))
# d= bool(int(b))
# print( c==False and d==False )

# # 다른 사람 풀이 참고2
# a, b = input().split()
# c= bool(int(a))
# d= bool(int(b))
# print( not (c or d) )
