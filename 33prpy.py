#1
a=424+2*(-2)*424+2*(-2)
print(a)

#2
a = 9 ** 19
b = float(9 ** 19)
c = int(b)
d = a - c
print(d)

#3

X = int(input())
Y = int(input())
print(X*60 + Y)

#4
X = int(input())
print (X//60)
print (X%60)

#5
X= int(input())
H= int(input())
M= int(input())
print(((H*60)+X+M)//60)
print((X+M)%60)

#6
A = int(input())
B = int(input())
H = int(input())
while A > B:
    print('Неккоректные данные')
    A = int(input())
    B = int(input())
    H = int(input())
if H<A:
    print('Недосып')
elif H > B:
    print('Пересып')
else:
    print('Это нормально')

#7
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный')
else:
    print('Обычный')


#8
a = float (input())
b = float (input())
c = str (input())
if c =='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/' and b==0:
    print("Деление на 0!")
elif c=='/' and b!=0:
    print(a/B)
elif c=='mod' and b==0:
    print('Деление на 0!')
elif c=='mod' and b!=0:
    print(a%b)
elif c=='pow':
    print(a**b)
elif c=='div' and b==0:
    print('Деление на 0!')
elif c=='div' and b!=0:
    print(a//b)

#10
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
  max = a
  if b>c:
    mid=b
    min=c
  else:
    mid=c
    min=b
  print(max)
  print(min)
  print(mid)
elif b>a and b>c:
  max=b
  if a>c:
    mid=a
    min=c
  else:
    mid=c
    min=a
  print(max)
  print(min)
  print(mid)
elif c>a and c>b:
  max=c
  if a>b:
    mid=a
    min=b
  else:
    mid=b
    min=a
  print(max)
  print(min)
  print(mid)
elif c==a and b==c:
  max=a
  min=b
  mid=c
  print(max)
  print(min)
  print(mid) 
elif c==a and (b>a or b>c):
  max=b
  min=c
  mid=a
  print(max)
  print(min)
  print(mid) 
elif c==a and (b<a or b<c):
  max=a
  min=b
  mid=c
  print(max)
  print(min)
  print(mid) 
elif a==b and (c<b or c<a):
  max=a
  min=c
  mid=b
  print(max)
  print(min)
  print(mid) 
elif a==b and (c>b or c>a):
  max=a
  min=b
  mid=c
  print(max)
  print(min)
  print(mid) 
elif c==b and (a>c or a>b):
  max=a
  min=c
  mid=b
  print(max)
  print(min)
  print(mid) 
elif c==b and (a<c or a<b):
  max=c
  min=a
  mid=b
  print(max)
  print(min)
  print(mid) 
  
  #12
s = str(input())
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
  print('Счастливый')
else:
  print('Обычный')

 #11
s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)
