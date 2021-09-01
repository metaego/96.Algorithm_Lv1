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