import time

print(r'(@) (@)')
print(r'(=^.^=)')
print(r'(-m-m-)')

print()
print('='*100)
num1 = 6
num2 = 2
print('6 + 2 =', num1+num2)
print('6 - 2 =', num1-num2)
print('6 * 2 =', num1*num2)
print('6 / 2 =', num1/num2)
# 6 + 2 = 8
# 6 - 2 = 4
# 6 * 2 = 12
# 6 / 2 = 3.0

print()
print('='*100)
# start_time = time.time()
str1= 'TTTTTTTTTT'
str2 = '    TT   '
print(str1)
print(str1)
print(str2)
print(str2)
# end_time = time.time()

# print('걸린시간 : ', end_time-start_time)

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
Fun Programming!
'''
print('Fun Programming!')

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
Programming! It's fun.
'''
print("Programming! It's fun.")

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
My name is Hong Gil Dong.
I am 13 years old.
'''

print("My name is Hong Gil Dong.")
print("I am 13 years old.")


print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
(@) (@)
(=^.^=)
(-m-m-)
'''
print(r'(@) (@)')
print(r'(=^.^=)')
print(r'(-m-m-)')

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
I can program well.
Dreams come true.
'''
print('I can program well.')
print('Dreams come true.')

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
My height
170
My weight
68.600000
'''
print('My height')
print(170)
print('My weight')
print(68.600000)

print()
print('='*100)

# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
5 Dan
5 * 2 = 10
'''
print('5 Dan')
print('5 * 2 = 10')


print()
print('='*100)

# 다음과 같이 출력되는 프로그램을 작성하라.
# (각 요소들은 10칸씩 공간을 확보하여 오른쪽으로 정렬하여 출력한다.)
'''
      item     count     price
       pen        20       100
      note         5        95
    eraser       110        97
'''
import time

start_time = time.time()
print("%10s" % "item"+"%10s" % "count"+"%10s" % "price")
print("%10s" % "pen"+"%10d" % 20+"%10d" % 100)
print("%10s" % "note"+"%10d" % 5+"%10d" % 95)
print("%10s" % "eraser"+"%10d" % 110+"%10d" % 97)
end_time = time.time()
print('걸린 시간: ', end_time-start_time)
# 걸린 시간:  0.000997304916381836

start_time2 = time.time()
print("{0:>10}".format("item")+"{0:>10}".format("count")+"{0:>10}".format("price"))
print("{0:>10}".format("pen")+"{0:>10}".format(20)+"{0:>10}".format(100))
print("{0:>10}".format("note")+"{0:>10}".format(5)+"{0:>10}".format(95))
print("{0:>10}".format("eraser")+"{0:>10}".format(110)+"{0:>10}".format(97))
end_time2 = time.time()
print('걸린 시간: ', end_time2-start_time2)
# 걸린 시간:  0.0009989738464355469

print('첫번째 방식이 두번째 방식보다 %f만큼 빠릅니다'% ((end_time2-start_time2)-(end_time-start_time)))


print()
print('='*100)
# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
My name is Hong
'''
print('My name is Hong')

print()
print('='*100)
# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
My hometown
Flowering mountain
'''
print('My hometown')
print('Flowering mountain')

print()
print('='*100)
# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
TTTTTTTTTT
TTTTTTTTTT
    TT
    TT
    TT
'''
str1= 'TTTTTTTTTT'
str2 = '    TT   '
print(str1)
print(str1)
print(str2)
print(str2)
print(str2)

print()
print('='*100)
# 아래 "출력예"와 같이 출력되는 프로그램을 작성하라.
'''
kor 90
mat 80
eng 100
sum 270
avg 90
'''
kor = 90
mat = 80
eng = 100
print('kor', kor)
print('mat', mat)
print('eng', eng)
print('sum', kor+mat+eng)
print('avg', (kor+mat+eng)//3)


print()
print('='*100)
# 다음 출력 예와 같이 모든 단어를 15칸씩 오른쪽에 맞추어 출력되는 프로그램을 작성하시오.
'''
          Seoul     10,312,545        +91,375
          Pusan      3,567,910         +5,868
        Incheon      2,758,296        +64,888
          Daegu      2,511,676        +17,230
        Gwangju      1,454,636        +29,774
'''
print('{0:>15}'.format('Seoul')+'{0:>15}'.format('10,312,545')+'{0:>15}'.format('+91,375'))
print('{0:>15}'.format('Pusan')+'{0:>15}'.format('3,567,910')+'{0:>15}'.format('+5,868'))
print('{0:>15}'.format('Incheon')+'{0:>15}'.format('2,758,296')+'{0:>15}'.format('+64,888'))
print('{0:>15}'.format('Daegu')+'{0:>15}'.format('2,511,676')+'{0:>15}'.format('+17,230'))
print('{0:>15}'.format('Gwangju')+'{0:>15}'.format('1,454,636')+'{0:>15}'.format('+29,774'))
