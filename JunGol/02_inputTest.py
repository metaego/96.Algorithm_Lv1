# 정수형 변수를 선언하고 -100을 대입하여 출력하는 프로그램을 작성하라.
'''
출력 예
-100
'''
num1 = -100
print(num1)

print()
print('='*100)
# 정수형 변수 2개를 선언하여 -1과 100을 대입한 후 아래와 같이 출력하는 프로그램을 작성하라.
'''
출력 예
-1
100
'''
num1 = -1
num2 = 100
print(num1)
print(num2)


print()
print('='*100)
# 두 개의 정수형 변수를 선언하고 값을 대입하여 아래와 같이 출력되는 프로그램을 작성하라.
'''
출력 예
55 - 10 = 45
2008 - 1999 = 9
'''
num1 = 55
num2 = 10
print('{} - {} = {}'.format(num1, num2, num1-num2))

num1 = 2008
num2 = 1999
print('{} - {} = {}'.format(num1, num2, num1-num2))

print()
print('='*100)
'''
추의 무게를 저장할 변수와 중력의 비율을 저장할 변수를 선언하고,
다음 두 값을 변수에 저장하여 곱셈 계산식을 출력하는 프로그램을 작성하라.

추의 무게 = 49, 중력의 비율 = 0.2683
'''
'''
출력 예
49 * 0.268300 = 13.146700
'''
weight = 49
gravity = 0.268300
# print('{} * {} = {}'.format(weight, gravity, weight*gravity))
print('%d * %.6f = %.6f'% (weight, gravity, weight*gravity))


print()
print('='*100)
'''
1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.

2.1야드와 10.5인치를 각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.​
'''
'''
출력 예
 2.1yd = 192.0cm
10.5in =  26.7cm
'''
ydPer = 91.44
inPer = 2.54
# print("2.1yd = %4.1fcm" % (2.1*ydPer))
# print("10.5in = %4.1fcm" % (10.5*inPer))
print("2.1yd = {0:0.1f}cm".format(2.1*ydPer))
print("10.5in = {0:0.1f}cm".format(10.5*inPer))
# 너무 화가 난다..... 분명 vscode에서는 출력이 잘 되는데, jungol에서는 프레젠테이션 에러가 난다..
# 왜 안되는지 이해가 되지 않는다.. 이유를 모르는데 에러만 나니까 너무 화가 난다.. ]
# 일단 패스

# 다른 사람 코드
# yd = 2.1
# _in = 10.5
# print("%4.1fyd = %5.1fcm" % (yd, yd*91.44))
# print("%4.1fin = %5.1fcm" % (_in, _in*2.54))


print()
print('='*100)
'''
키를 입력받아 출력하는 프로그램을 작성하라.

(입력할때 "height = " 문장을 먼저 출력하고 키를 입력 받아야 합니다.)
'''
'''
입력 예
height = 170

출력 예
Your height is 170cm.
'''
# height = int(input("height = "))
# print('Your height is {}cm.'.format(height))


print()
print('='*100)
'''
두 개의 정수를 입력 받아 곱과 몫을 출력하시오.
(먼저 입력 받는 수가 항상 크며 입력되는 두 정수는 1이상 500이하이다.)
'''
'''
입력 예
16 5

출력 예
16 * 5 = 80
16 / 5 = 3

'''

# num1, num2 = map(int, input().split( ))

# num1, num2 = int(input('')).split( )
print('{} * {} = {}'.format(num1, num2, num1*num2))
print('{} / {} = {}'.format(num1, num2, num1//num2))
# 다른 사람 코드
# a, b = input().split( )
# print("%d * %d = %d" % (int(a), int(b), int(a)*int(b)))
# print("%d / %d = %d" % (int(a), int(b), int(a)/int(b)))


print()
print('='*100)
'''
실수 2개와 한 개의 문자를 입력 받아 출력하되 실수는 반올림하여 소수 둘째자리까지 출력하는 프로그램을작성하시오.
(C, C++, Java 의 경우 실수는 "double"로 선언하세요.)
'''
'''
입력 예
12.2536
526.129535
A

출력 예
12.25
526.13
A
'''

# flatNum1 = 12.2536
# flatNum2 = 526.129535
# varchar = 'A'

# flatNum1 = float(input())
# flatNum2 = float(input())
# varchar = input()

# print('%.2f' % round(flatNum1, 2))
# print('%.2f' % round(flatNum2, 2))
# print(varchar)


print()
print('='*100)
'''
세 개의 실수를 입력 받아 반올림하여 소수 셋째 자리까지 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
1.2568
95.21438
526.851364

출력 예
1.257
95.214
526.851
'''
# floatNum1 = float(input())
# floatNum2 = float(input())
# floatNum3 = float(input())

# print('%.3f' % round(floatNum1, 3))
# print('%.3f' % round(floatNum2, 3))
# print('%.3f' % round(floatNum3, 3))



print()
print('='*100)
'''
세 개의 정수형 변수를 선언하고 각 변수에 10 20 30을 대입한 후 
그 변수를 이용하여 출력 예와 같이 출력하는 프로그램을 작성하시오.
'''
'''
출력 예
10 + 20 = 30
'''
num1 = 10
num2 = 20
num3 = 30
print(f'{num1} + {num2} = {num3}')



print()
print('='*100)
'''
실수형 변수를 2개 선언한 후 각각에 80.5 22.34를 대입한 후 두 수의 합을 구하여 
각각의 숫자를 10칸씩 오른쪽에 맞추어 소수 둘째자리까지 출력하는 프로그램을 작성하시오.
'''
'''
출력 예
     80.50     22.34    102.84
'''
num1 = 80.5
num2 = 22.34

print('%10.2f%10.2f%10.2f' % (num1, num2, num1+num2))



print()
print('='*100)
'''
정수형 변수 한 개를 선언하여 50을 대입하고 
실수형 변수 한 개를 선언하여 100.12를 대입한 후 
다음과 같이 출력되는 프로그램을 작성하시오.
(결과값은 소수점 이하에서 반올림) 
'''
'''
출력 예
100.12 * 50 = 5006
'''
intnum = 50
floatnum = 100.12
print(f'{floatnum} * {intnum} = {int(round(floatnum*intnum, 1))}')




print()
print('='*100)
'''
세 개의 정수를 입력받아 합과 평균을 출력하는 프로그램을 작성하시오.
(단 평균은 소수 이하를 버림하여 정수 부분만 출력한다.)
'''
'''
입력 예
10 20 30

출력 예
sum = 170
avg = 56
'''

# n1, n2, n3 = map(int, input().split())
# print('sum =', n1 +n2 +n3)
# print('avg =', (n1 +n2 +n3)//3)


print()
print('='*100)
'''
실수의 yard(야드)를 입력받아 cm(센티미터)로 환산하여 
입력값과 환산한 값을 출력 예와 같이 소수 둘째자리에서 반올림하여 
첫째자리까지 출력하는 프로그램을 작성하시오. (단 1야드 = 91.44cm로 한다.)  
입력은 "yard? "라고 먼저 출력하고, 실수를 입력받는다.  실수는 "double"로 한다.
'''
'''
입력 예
yard? 10.1

출력 예
10.1yard = 923.5cm
'''
# yard = float(input("yard? "))
# yardPerCM = 91.44
# print('%.1fyard = %.1fcm' % (yard, round(yard*yardPerCM, 2)))



print()
print('='*100)
'''
1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
2.1야드와 10.5인치를 각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.​
'''
'''
출력 예
 2.1yd = 192.0cm
10.5in =  26.7cm
'''
yd = 91.44
inch = 2.54
print('%6s = %5.1fcm' % ('2.1yd', 2.1*yd))
print('%6s = %5.1fcm' % ('10.5in', 10.5*inch))
