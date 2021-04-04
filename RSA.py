import random
p =7# duża np.49667 albo int(input())
q =13 # duża np.49669 albo int(input()) obie liczby muszą być pierwsze
n = p*q
Eu=(p-1)*(q-1)
war= True
def NWD(a,b):
    while war:
        if a==b:
            return a
        elif a>b:
            a=a-b
        else:
            b=b-a
war=True
d=0
while war:
    d=random.randrange(3,Eu-1)
    if NWD(d,Eu)==1:
        war=False
# wyliczanie elementu odwrotnego w pierścieniu Eu
a=Eu
b=d
nwd=b
q=int(a/b)
r=a-q*b
xi2=1
xi1=0
xi=1
yi2=0
yi1=1
yi=(q-1)
while r!=0:
    a=b
    b=r
    xi=xi2-q*xi1
    yi=yi2-q*yi1
    xi2=xi1
    yi2=yi1
    xi1=xi
    yi1=yi
    nwd=r
    q=int(a/b)
    r=a-q*b
e=yi
if e<0:
    e=e+Eu
#część użytkowa programu
print('podaj liczbe do zaszyfrowania mniejszą od ',n)
l=int(input())
print('szyfrowanie')
sz=pow(l,d,n)
print(sz, l**d)
print('deszyfrowanie')
desz=pow(sz,e,n)
print(desz)
