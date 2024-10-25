                                  # SEIVE only for 10^7

"""a,b=map(int,input().split())                 
primes=[1]*(b+1)
primes[0]=1
primes[1]=0
for i in range(2,b+1):
    if primes[i]==1:
        for j in range(i+i,b+1,i):
            primes[j]=0
for i in range(a,b+1):
    if primes[i]==1:
        print(i,end=" ")"""

                                  # SEGMENTED SEIVE used for 10^12
"""def sieve(n):
    primes=[1]*(n+1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2,n+1):
        if primes[i] == 1:
            for j in range(i+i,n+1,i):
                primes[j] = 0
    if primes[n] == 1:
        return True
    return False
l = 160
r = 180
pr_mul=[]
ref = int(r**0.5)
for i in range(2,ref+1):
    if sieve(i):
        pr_mul.append(i)
dum_ary = [1]*(r-l+1)
for i in pr_mul:
    frst_mul = l//i*i
    if frst_mul<l:frst_mul+=i
    #print(frst_mul,"#")
    if frst_mul<=3:
        frst_mul+=frst_mul
        dum_ary[0] = 0
    for j in range(frst_mul,r,i):
        dum_ary[j-l] = 0
for k in range(l,r):
    if dum_ary[k-l] == 1:
        print(k,end = ",")"""

                             # prime Factorization Using Seive
"""n = 10
lt = list(range(n+1))
#print(lt)
for i in range(2,n+1):
    if lt[i] == i:
        for j in range(i+i,n+1,i):
            if lt[j] == j:
                lt[j] = i
while n>1:
    print(lt[n])
    n//=lt[n]"""

                                 # selection sort
                                 # Time complexity is O(N**2)
def sel_sort(arr):
    for i in range(len(arr)-1):
        minn = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minn]:
                minn = j
        arr[i],arr[minn] = arr[minn],arr[i]
    return arr
arr = [9,8,1,2,41,5,6,2]
#print(sel_sort(arr))
            


                                # BUBBLE SORT
                                # Time complexity is O(N**2)
                                # but if the array is sorted the time complexity
                                # of bubble sort is O(N) by small modification
                                # by adding did_swap, if no swapping is done in
                                # second loop then array is sorted we can break
                                # the loop
def bub_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        did_swap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                did_swap = 1
        if did_swap == 0:
            break
    return arr
#arr = [9,8,1,2,41,5,6,2]
arr = [1,2,5,6,8,9]
#print(bub_sort(arr))


                               # insertion Sort
                               # Time complexity is O(N**2)
                               # but if the array is sorted the time complexity
                               # of insertion sort is O(N)

def ins_sort(arr):
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr
arr = [5,1,2,4,9,4,7,2,3]
#print(ins_sort(arr))


                                # Merge Sort
                                # Time complexity is Nlog(N)
                                # Space complexity is O(N)


def merge(arr,low,mid,high):
    temp = []
    lft = low
    rgt = mid+1
    while lft<=mid and rgt<=high:
        if arr[lft]<=arr[rgt]:
            temp.append(arr[lft])
            lft+=1
        else:
            temp.append(arr[rgt])
            rgt+=1
    while lft<=mid:
        temp.append(arr[lft])
        lft+=1
    while rgt<=high:
        temp.append(arr[rgt])
        rgt+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]


def merge_sort(arr,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
arr = [1,2,9,6,3,5,7,8,2]
low = 0
high = len(arr)-1
merge_sort(arr,low,high)
print(arr)

                               # Quick Sort Algorithm

def partition(arr,low,high):
    piv = low
    lft = low
    rgt = high
    while lft<rgt:
        while arr[lft]<=arr[piv] and lft<high:
            lft+=1

        while arr[rgt] > arr[piv] and rgt>low:
            rgt-=1

        if lft<rgt:
            arr[lft],arr[rgt] = arr[rgt],arr[lft]

    arr[piv],arr[rgt] = arr[rgt],arr[piv]
    return rgt


def quick_sort(arr,low,high):
    if low<=high:
        part = partition(arr,low,high)
        quick_sort(arr,low,part-1)
        quick_sort(arr,part+1,high)


arr = [1,2,9,6,3,5,7,8,2]
# print(arr)
low = 0
high = len(arr)-1
quick_sort(arr,low,high)
print(arr)
            

                                 # BINARY SEARCH

"""def sai(l,n):
    low=0
    high=len(l)-1
    while low <= high:
        mid= (low + high) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            low=mid+1
        elif l[mid] > n:
            high = mid-1
    return -1

l=[1,2,3,4,5,6,8,9]
n=1
print(sai(l,n))"""

                                 # reverse a integer
def rev(n):
    s=0
    while n:
        a=n%10
        s=s*10+a
        n=n//10
        return s
"""n=1619
print(rev(n))"""
                        
                              # subset
def sub_set(l,n):
    for i in range(1<<n):
        for j in range(n):
            if (i&(1<<j)):
                print (l[j],end=" ")
        print()
    return 
#l=[3,5,6,7]
#n=4
                              # RECURSION
def dig_cnt(n):
    if n==0:
        return 0
    else:
        return (1 + dig_cnt(n//10))
#n=1990
#print(dig_cnt(n))

def prnt_num(n):
    if n==0:
        return
    else:
        return prnt_num(n-1)
        print(n)
"""n=5
print(prnt_num(n))"""


                            # SLIDING WINDOW

def max_sum(arr,k):
    n=len(arr)
    if n<k:
        return "Invalid Array"
    else:
        wind_sum=sum(arr[:k])
        maxx_sum=wind_sum
        for i in range(n-k):
            wind_sum=wind_sum - arr[i] + arr[i+k]
            maxx_sum=max(maxx_sum,wind_sum)
        return maxx_sum
"""arr=[16,12,9,19,11,8]
k=3
print(max_sum(arr,k))"""

     # recursion program to check weather the list is sorted or not * * *

def lst_srt(arr,n):
    if n==0 or n==1:
        return True
    return arr[n-1] >= arr[n-2] and lst_srt(arr,n-1)
arr=[1,2,3,5,8,9]
n=len(arr)
"""if lst_srt(arr,n):
    print("YES")
else:
    print("NO")"""


        # Longest common Substring (DP)

"""s1 = "ABCDGHR"
s2 = "OACDGHW"
ln = max(len(s1),len(s2))+1
dp = [[-1 for i in range(ln)] for j in range(ln)]
for i in range(ln):
    dp[0][i] = 0
    dp[i][0] = 0
maxx = -1
i1,i2 = -1,-1
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            # print(s1[i-1],s2[j-1])
            dp[i][j] = 1+dp[i-1][j-1]
            if dp[i][j] > maxx:
                maxx = dp[i][j]
                i1,i2 = i,j
        else:
            dp[i][j] = 0
print(maxx) #---> it gives the length

ans = ""
while dp[i1][i2]!=0:
    ans+=s1[i1-1]
    i1-=1
    i2-=1
print(ans[::-1])# it gives the substring"""

                # recursion program to give nth fibnoci number
def fibb_n(n):
    if n<=1:
        return n
    return fibb_n(n-2) + fibb_n(n-1)
"""n=0
print(fibb_n(n))"""

def bin_rec(arr,high,low,find):
    if high < low:
        return -1
    mid = (high + low)//2
    if arr[mid] == find:
        return mid
    if arr[mid] < find:
        low = mid+1
    else:
        high = mid-1
    return bin_rec(arr,high,low,find)
"""arr=[1,2,5,8,9,11,15]
find=16
low=0
high=len(arr)-1
print(bin_rec(arr,high,low,find))"""

            # fibbnocci using list compression

#fibb=[0,1]
#[fibb.append(fibb[-1]+fibb[-2]) for i in range(4)]
#print(fibb)


                 # Binary exponentiation  (to find the power of a Number)

def bi_exp(a,b):
    ans = 1
    while b:
        if b%2 == 0:
            a = a*a
            b/=2
        else:
            ans = ans * a
            b-=1
    return ans
#print(bi_exp(5,2))


           # Implementation of Trie (WORD_INSERT,WORD_SEARCH,PREFIX_SEARCH)

"""class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfword = True
    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfword
    def prefix(self,pre):
        cur = self.root
        for c in pre:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True"""










































