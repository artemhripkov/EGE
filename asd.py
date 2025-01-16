# 2 задание
from itertools import *
def f(x,y,w,z):
  return (x==(not y))<=((x and w)==z)
for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
    table = [(1,1,a1,a2),(1,1,a3,1),(a4,1,1,a5)] 
    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in table]==[0,0,0]: 
                print(p)
############################
# 16 задание
from sys import * 
setrecursion limit(10000)
def f(n):
    if n<=2: 
        return 1
    if n>2:
        return n*f(n-2)
print(f(5000)/f(4994))
#############################
# 17 задание
a = [int(x) for x in open('17-243.txt')]

S = sum([int(i) for x in a if x % 49 == 0 for i in str(x)])
ans = []
for i in range(len(a) - 1):
    if (a[i] > S and (not a[i + 1] > S) and a[i + 1] % 10 == 7) or \
            (a[i + 1] > S and (not a[i] > S) and a[i] % 10 == 7):
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))
############################
# 19-21 задание
def f(a,b,m):
    if a+b>=231: return m%2==0
    if m==0: return 0
    h = [f(a+2,b,m-1),f(a*2,b,m-1),f(a,b+2,m-1),f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all|(h)
print('19)',[s for s in range(1,214) if f(17,s,2)]) #all->any
print('20)',[s for s in range(1,214) if not f(17,s,1) and f(17,s,3)])
print('21)',[s for s in range(1,214) if not f(17,s,2) and f(17,s,4)])
############################
# 23 задание
from functools import *
alru_cache(None)
def f(c,e):
    if c>e: \
        return 0
    if c==e:
        return 1
    if c<e:
        return f(c+1, e)+f(2*c, e)+f(2*c+1,e) 
print(f(4,218))
#############################
# 25 задание
def div(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for x in range(244143, 367821+1):
    #если число является квадратом целого числа 
    if int(x**0.5)**2 == x:
        d = div(x)
        if len(d)==5:
            print(d[3],d[4])


