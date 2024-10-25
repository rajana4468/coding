"""def R_C(n):
    dic={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
    dic1=dict(reversed(list(dic.items())))
    res=""
    for i,j in dic1.items():
        if n//j:
            count = n//j
            res+=(i*count)
            n=n%j
    return res
n=int(input())
print(R_C(n))"""

##i=0
##j=1
##while i < len(p) and j < len(p):
##    if (j > i) and p[j] <= p[i]:
##        p[i] = (p[i] - p[j])
##        i+=1
##        j=i+1
##    else:
##        j+=1
##        if j==len(p)-1:
##            i+=1
##            j=i+1
        
"""l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()"""

"""import numpy as np
r=int(input())
c=int(input())
matrix=list(map(int,input().split()))
matrix=np.array(matrix).reshape(r,c)
print(matrix)"""

"""mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]
r= len(mat)
k=3
op=[]
for i in range(r):
    op.append([mat[i].count(1),i])
op.sort()
print(op)
print([k for j,k in op[:k]])"""

"""arr = [[0, 1, 1, 1],
        [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
op=[]
for i,j in enumerate(arr) :
    op.append([sum(j),i])
print(max(op))"""

"""fib=[0,1]
[fib.append(fib[-2] + fib[-1]) for i in range(int(input()))]
print(fib)"""

"""import collections
op=[]
n=[3,2,3]
c=collections.Counter(n)
print(c)
for i,j in c.items():
    if j==len(n)//3:
        op.append(i)
print(op)"""

"""nums = "codeleet"
index = [4,5,6,7,0,2,1,3]
tg=[]
for i,j in zip(nums,index):
    tg[j:j] = [i]
    print(tg)"""


n=int(input())
k=((list(range(1,n+1))))
print(k)
pro=1
for i in k:
    pro*=i
print(pro)























                                                                    
