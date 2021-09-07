'''
리스트를 만들고, 출력하여 
출력 예와 같이 나오도록 하는 프로그램을 작성하라.
'''
'''
출력 예
['Salad', 'Pizza', 'Chicken', 'Soup']
'''
# lst = ['Salad', 'Pizza', 'Chicken', 'Soup']
# print(lst)

print()
print('='*100)
'''
'Python', 'is', 'exciting' 세 문자열로 이루어진 리스트를 만들고, 
다음과 같이 출력하는 프로그램을 작성하라.​
'''
'''
출력 예
Python is exciting
'''
lst = ['Python', 'is', 'exciting']
print(' '.join(lst))

# 추가로 문자열을 리스트로 변환하는 방법은
# str변수명.split(" ")

# , 로 문자열의 내용을 구분하고 싶을 때
# str변수명.split(",")  

# 문자열을 글자 단위로 분리하여 리스트로 변환 
# data = list("ABC")
# print(data)
# print(*data) 


print()
print('='*100)
'''
세 개의 리스트를 만들어 아래 순서대로 합병하여 출력하는 프로그램을 작성하라.
[첫 번째 리스트][세 번째 리스트][세 번째 리스트][세 번째 리스트][두 번째 리스트]
첫 번째 리스트:[1, 2, 3]
두 번째 리스트:[2, 4, 6]
세 번째 리스트:[3, 6, 9] 
'''
'''
출력 예
[1, 2, 3, 3, 6, 9, 3, 6, 9, 3, 6, 9, 2, 4, 6]
'''
# lst1 = [1, 2, 3]
# lst2 = [2, 4, 6]
# lst3 = [3, 6, 9] 
# print(lst1+lst3*3+lst2)

print()
print('='*100)
'''
리스트를 하나 만들어 [1, 2]로 초기화하고, 
추가로 정수를 하나 더 입력 받아 리스트 끝에 추가한 후 
역순으로 출력하는 프로그램을 작성하시오.
'''
# num = int(input())
# lst = [1, 2]
# lst.append(num)
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])


print()
print('='*100)
'''
문자열을 하나 입력받아서 그 문자열의 맨 앞에 있는 문자를 출력한 후, 
그 문자열을 리스트로 변환한 후에 
해당 리스트의 앞에서부터 세 번째 문자를 출력하는 프로그램을 작성하라. 
(입력되는 문자열은 항상 길이가 3 이상이라고 가정한다.)
'''
'''
입력 예
Eagle

출력 예
E
g
'''
# txt = input()
# print(txt[0])
# lst = "".join(txt)
# print(lst[2])


print()
print('='*100)
'''
원소 6개짜리 리스트를 입력받아 생성한 후, 
인덱스를 입력 받아 
입력받은 인덱스부터 맨 마지막까지의 부분 리스트를 출력하는 
프로그램을 작성하라.
'''
'''
입력 예
Element? Seoul
Element? New York City	
Element? Tokyo	
Element? Beijing	
Element? London	
Element? Paris	
Index? 3

출력 예
['Beijing', 'London', 'Paris']
'''
lst = []
for i in range(6):
    lst.append(str(input('Element? ')))
idx_number = int(input('Index? '))
print(lst[idx_number:])