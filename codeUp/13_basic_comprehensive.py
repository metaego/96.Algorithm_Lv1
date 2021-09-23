# 기초_종합
'''
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

예시
#다음 코드는 홀 수만 더해 출력한다.
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==1 :
    s += i

print(s)

참고
while 이나 for 반복실행구조를 이용할 수 있다.
다른 방법이나 while 반복실행구조를 이용해서도 성공시켜 보자.
'''
# n = int(input())
# c = 0
# for i in range(n+1):
#     if i%2 == 0:
#         c += i
# print(c)
'''
영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.
'''
# input_chr = input()
# while input_chr != 'q':
#     print(input_chr)
#     input_chr = input()
# if input_chr == 'q':
#     print(input_chr)

# 다른 사람 풀이
# while True:
#     x = input()
#     print(x)
#     if x == 'q':
#         break

'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.
'''
# n = int(input())
# c = 0
# for i in range(n+1):
#     if c >= n:
#         # print(c, i)
#         break
#     else:
#         c += i
#         # print(c, i)
# print(i-1)

# 다른 사람 풀이1
# n = int(input())
# s = 0
# t = 0
# while s < n:
#     t += 1
#     s += t
# print(t)

'''
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.

예시
...
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)
...

참고
위 코드는
바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에
안쪽의 j 값이 다시 1부터 m까지 변하며 출력되는 코드이다.

조건선택 실행구조 안에 다른 조건선택 실행구조를 넣어 처리할 수 있는 것과 마찬가지로
반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.

원하는 형태로 실행 구조를 결합하거나 중첩시킬 수 있다.
'''
# n, m = map(int, input().split())
# for i in range(1, n+1) :
#       for j in range(1, m+1) :
#         print(i, j)

'''
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.
    >> 영일아 왜 그거 궁금해하고 그래,,,,,,,ㅠ
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

예시
...
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
...

참고
print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 
공백없이 모두 붙여 출력된다.
작은 따옴표 2개 '' 또는 큰 따옴표 2개 "" 는 
아무 문자도 없는 빈문자열(empty string)을 의미한다.
'''
# n = int(input(), 16)
# for i in range(1, 16):
#     print('%X*%X=%X' % (n, i, n*i))
'''
친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

** 3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 
수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 

참고 
...
for i in range(1, n+1) :
  if i%10==3 :
    print("X", end=' ')    #출력 후 공백문자(빈칸, ' ')로 끝냄
...
'''
# n = int(input())
# for i in range(1, n+1):
#     if i%10 in [3, 6, 9]:
#         print('X', end = ' ')
#     else:
#         print(i, end = ' ')
'''
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 
만들 수 있는 색의 가짓 수를 계산해보자.  

**모니터, 스마트폰과 같은 디스플레이에서 각 픽셀의 색을 만들어내기 위해서 
r, g, b 색을 조합할 수 있다.
**픽셀(pixel)은 그림(picture)을 구성하는 셀(cell)에서 이름이 만들어졌다.
'''
# count = 0
# r, g, b = map(int, input().split())
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print('{} {} {}'.format(i,j,k))
#             count += 1 
# print(count)

'''
소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크하고,
한 번씩 체크할 때 마다 그 값을 정수값으로 바꾸어 저장하는 방식으로 
소리를 파일로 저장할 수 있다.

값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.

실제로, 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
44100*16*2*1/8/1024/1024 로 계산하면 약 0.168 MB 정도가 필요하다.

이렇게 녹음하는 방식을 PCM(Pulse Code Modulation) 방법이라고 하는데,
압축하지 않은 순수한(raw) 소리 데이터 파일은 대표적으로 *.wav 가 있다.

**
      8 bit(비트)           = 1byte(바이트)       # 8bit=1Byte
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)     = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)
'''
'''
1초 동안 마이크로 소리강약을 체크하는 횟수를 h
한 번 체크한 값을 저장할 때 사용하는 비트수를 b
좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
녹음할 시간(초) s
'''
# h, b, c, s = map(int, input().split())
# print('%.1f MB' % (h*b*c*s/8/1024/1024))

'''
이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다.

가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을
빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장하는 것인데,

예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면,

한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서
총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.

그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데,
1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
저장 용량을 계산할 수 있다.

이렇게 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이
*.bmp 파일이며, 비트로 그림을 구성한다고 하여 비트맵 방식 또는 래스터 방식이라고 한다.

이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

예를 들어
일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
24비트(rgb 각각 8비트씩 3개)로 저장하려면
1024 * 768 * 24 bit의 저장공간이 필요한데,
1024*768*24/8/1024/1024 로 계산하면 약 2.25 MB 정도가 필요하다.

실제 그런지 확인하고 싶다면, 간단한 그림 편집/수정 프로그램을 통해 확인할 수 있다.

**
      8 bit(비트)           = 1byte(바이트)     #       8bit=1Byte
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)     = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)
'''
# w, h, b = map(int, input().split())
# print('%.2f MB' % (w*h*b/8/1024/1024))
# n = int(input())
# s = 0
# c = 0
# while True :
#     s += c
#     c += 1
#     if s>=n :
#         break
# print(s)

'''
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.

예를 들면,
1 2 4 5 7 8 10 11 13 14 ...
와 같이 출력하는 것이다.

예시
...
for i in range(1, n+1) :
  if i%2==0 :
    continue            #다음 반복 단계로 넘어간다.
  print(i, end=' ')    #i가 짝수가 아닐 때만 실행된다.
...
위 코드는 홀 수만 출력하는 예시이다.

참고
조건문이나 반복문의 코드블록 안에서 continue 가 실행되면,
반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다.
즉, 반복 블록의 나머지 부분은 실행되지 않고, 
다음 단계의 반복을 계속(continue)하는 것이다.
'''
# n = int(input())
# for i in range(n+1):
#     if i%3 == 0:
#         continue
#     else:
#         print(i, end= ' ')

'''
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

예를 들어
1 4 7 10 13 16 19 22 25 ... 은
1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여

등차(차이가 같다의 한문 말) 수열이라고 한다. 
(등차수열 : arithmetic progression/sequence)
수열을 알게 된 영일이는 갑자기 궁금해졌다.

"그럼.... 123번째 나오는 수는 뭘까?"

영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.
'''
# a, d, n = map(int, input().split())
# for i in range(a, n+1):
#     s = a + (i-1)*d
# print(s)


'''
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

예를 들어
2 6 18 54 162 486 ... 은
2부터 시작해 이전에 만든 수에 3을 곱해 다음 수를 만든 수열이다.

이러한 것을 수학에서는 앞뒤 수들의 비율이 같다고 하여
등비(비율이 같다의 한문 말) 수열이라고 한다. 
(등비수열 : geometric progression/sequence)

등비 수열을 알게된 영일이는 갑자기 궁금해졌다.
"그럼.... 13번째 나오는 수는 뭘까?"
영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.
'''
# a, r, n = map(int, input().split())
# for i in range(a, n+1):
#     t = a*r**(i-1)
# print(t)
'''
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

예를 들어
1 -1 3 -5 11 -21 43 ... 은
1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.

이런 이상한 수열을 알게 된 영일이는 또 궁금해졌다.
"그럼.... 13번째 나오는 수는 뭘까?"

영일이는 물론 수학을 아주 잘하지만 이런 문제는 본 적이 거의 없었다...
그래서 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째 수를 출력하는 프로그램을 만들어보자.
'''
# a, m, d, n = map(int, input().split())
# for i in range(a,a+n):
#     if i == a:
#         s = a
#     else:
#         s = s * m + d
# print(s)

# # 다른 사람 풀이1
# a, m, d, n = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)
# for i in range(1, n) :
#   a = a*m+d
# print(a)

'''
온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

자! 여기서...잠깐..
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

갑자기 힌트?
왠지 어려워 보이지 않는가?
수학에서 배운 최소공배수를 생각한 사람들도 있을 것이다. 
하지만, 정보에서 배우고 경험하는
정보과학의 세상은 때때로 컴퓨터의 힘을 빌려 간단한 방법으로 해결할 수 있게 한다.

아래의 코드를 읽고 이해한 후 도전해 보자.
day는 날 수, a/b/c는 방문 주기이다.
...
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
...

물론, 아주 많은 다양한 방법이 있을 수 있다.

정보과학의 문제해결에 있어서 정답은?
하나가 아니라 주어진 시간/기억공간으로 정확한 결과를 얻을 수 있는 모든 방법이다.

따라서, 모든 문제들에는 정답이 하나뿐만이 아니다.
새로운, 더 빠른, 더 간단한 방법을 다양하게 생각해보고 
여러가지 방법으로 도전해 볼 수 있다.
'''
# a, b, c = map(int, input().split())
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)

'''
정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

선생님은 출석부를 보고 번호를 부르는데,
학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
이름과 얼굴을 빨리 익히려고 하는 것이다.

출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

예시
n = int(input())      
#개수를 입력받아 n에 정수로 저장

a = input().split()  
#공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       
  #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                     
#d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.

for i in range(24) :  
    #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)        
  #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :    
    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  
    #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

참고
- d = []              
#어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기

- d.append(값)  
#d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 

- d[a[i]] += 1     
# 2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 
# 1번 카운트 1개 증가..

어떤 값을 기록했다가 다시 사용할 필요가 있을 때, 
필요한 변수(variable)를 만들어 사용하는 것처럼,
여러 개의 값을 하나로 묶어 목록으로 기록했다가 다시 사용할 필요가 있을 때, 
리스트(list)를 만들어 사용할 수 있다.
리스트는 변수들을 모아 놓은 변수라고 생각할 수도 있고, 
참조번호를 이용해 간단하고 편리하게 사용할 수 있다.
'''
# n = int(input())      
# a = input().split()
# for i in range(n):
#     a[i] = int(a[i])  

# d = []                     

# for i in range(24) :  
#   d.append(0)        

# for i in range(n) :    
#   d[a[i]] += 1

# for i in range(1, 24) :  
#   print(d[i], end=' ')

'''
정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.

출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

예시
...
for i in range(n-1, -1, -1) :
  print(a[i], end=' ')
...

참고
번호를 부른 순서를 리스트에 순서대로 기록해 두었다가, 
기록한 값들을 거꾸로 출력하면 된다.
range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0
'''
# n = int(input())
# a = input().split()
# for i in range(n-1, -1, -1):
#     print(a[i], end= ' ')
'''
정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단, 
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.

참고
리스트에 출석 번호를 기록해 두었다가, 그 중에서 가장 작은 값을 찾아내면 된다.
그런데, 가장 작은 값은 어떻게 어떤 것과 비교하고, 어떻게 찾아야 할까?
'''
# n = int(input())
# lst = input().split()
# for i in range(n):
#     lst[i] = int(lst[i])
# lower_number = lst[0]

# for i in range(n):
#     if lst[i] < lower_number :
#         lower_number = lst[i]
#     else:
#         continue
# print(lower_number)

# # 다른 사람 풀이1
# n = int(input())
# a = input().split()

# for i in range(n) :
#   a[i] = int(a[i])

# min = a[0]
# for i in range(0, n) :
#   if a[i] < min :
#     min = a[i]

# print(min)


'''
기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

예시
d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기
  for j in range(20) : 
    d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈

참고
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고, 더 확장한 n차원의 리스트도 만들 수 있다.

...
d=[]
for i in range(20) : 
  d.append([])
  for j in range(20) :  
    d[i].append(0)
... 

위와 같이, 모두 0이 채워진 2차원 리스트를 만드는 코드를 아래와 같은 방법으로 짧게 만들 수도 있다.
... [0 for j in range(20)]  #20개의 0이 들어간 [0, 0, 0, ... , 0, 0, 0] 리스트 
아래처럼 작성하면 위와 같은 리스트가 20개가 들어간 리스트를 한 번에 만들어 준다.

d = [[0 for j in range(20)] for i in range(20)]

이러한 리스트 생성 방식을 List Comprehensions 라고 한다.
'''
# d=[]                      
# for i in range(20) :
#   d.append([])         #리스트 안에 다른 리스트 추가해 넣기
#   for j in range(20) : 
#     d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기
# # print(len(d))

# n = int(input())
# for i in range(n) :
#   x, y = input().split()
#   d[int(x)][int(y)] = 1

# for i in range(1, 20) :
#   for j in range(1, 20) : 
#     print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
#   print()

# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)

# n = int(input())

# for i in range(n):
#     x, y = map(int, input().split())
#     d[x][y] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=' ')
#     print()

'''

'''
# d=[]

# for i in range(20):
#     d.append(input().split())

# n = int(input())

# # for i in range(n):
# #     x, y = map(int, input().split())
# #     for j in range(1, 20):
# #         if d[x][j] == 0:
# #             d[x][j] = 1
# #         else:
# #             d[x][j] = 0

# #         if d[j][y] == 0:
# #             d[j][y] = 1
# #         else:
# #             d[j][y] = 0

# for i in range(n) :
#     x,y=input().split()
#     for j in range(1, 20) :
#         if d[j][int(y)]==0 :
#             d[j][int(y)-1]=1
#         else :
#             d[j][int(y)]=0

#         if d[int(x)][j]==0 :
#             d[int(x)][j]=1
#         else :
#             d[int(x)][j]=0


# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=' ')
#     print()

'''
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)


격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''
w, h = map(int, input().split())
m = []
for i in range(h):
    m.append([])
    for j in range(w):
        m[i].append(0)
    
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for i in range(l):
        m[x-1][y-1]=0
        # 모르겠다..일단 보류


