'''
2개의 실수(double)를 입력 받아서 
두 수의 곱을 정수로 변환한 결과값과 
두 수를 각각 정수로 변환하여 곱을 구한 결과값을 출력하는 프로그램을 작성하고 
프로그램 내용에 관한 설명을 주석으로 표시하시오.
'''
'''
입력 예
3.4 5.65

출력 예
19 15
'''
# num1, num2 = map(float, input().split())

# # 두 수의 곱을 정수로 변환한 결과값
# print(int(num1*num2))

# # 두 수를 각각 정수로 변환하여 곱을 구한 결과값
# print(int(num1)*int(num2))
print()
print('='*100)
'''
2개의 정수를 입력 받아서 첫 번째 수를 두 번째 수로 나눈 몫을 출력하고, 
첫 번째 수를 실수로 변환하여 두 번째 수로 나눈 값을 구한 후 반올림하여 소수 둘째 자리까지 출력하는 프로그램을 작성하고, 
프로그램 내용에 관한 설명을 주석으로 표시하시오.
'''
'''
입력 예
11 3

출력 예
3 3.67
'''
# num1, num2 = map(int, input().split())

# # 첫번째 수를 두번째 수로 나눈 몫 출력
# print(num1//num2)

# # 첫 번째 수를 실수로 변환하여 두 번째 수로 나눈 값을 구한 후 반올림하여 소수 둘째 자리까지 출력
# print('%.2f' % (round(float(num1)/num2, 2)))

print()
print('='*100)
'''
정수로 된 3과목의 점수를 입력받아 평균을 구한 후 
반올림하여 소수 첫째자리까지 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
70 95 65

출력 예
76.7
'''
# sub1, sub2, sub3 = map(int, input().split())
# print('%.1f' % ((sub1+sub2+sub3)/3))


print()
print('='*100)
'''
실수로 된 3과목의 점수를 입력받아 
총점은 정수부분의 합계를 출력하고 
평균은 실수의 평균을 구한 뒤 
정수부분만 출력하는 프로그램을 작성하시오.
'''
'''
입력 예
70.5 95.5 68.5

출력 예
sum 233
avg 78
'''
# sub1, sub2, sub3 = map(float, input().split())
# print('sum {}'.format(int(sub1) + int(sub2)+ int(sub3)))
# print('avg {}'.format(int((sub1+sub2+sub3)/3)))

print()
print('='*100)
