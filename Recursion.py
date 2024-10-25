
                     # Reverse an Array with parameters passing 

"""def rev_arr(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    rev_arr(arr,l+1,r-1)
n = 5
arr = [5,1,4,8,7]
print("Initial Array:",arr)
rev_arr(arr,0,n-1)
print("Reversed Array:",arr)"""


                 # Reverse an Array with single variable as a Parameter

"""def rev_arr(arr,i,n):
    if i >= n//2:
        return
    #print(i)
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    rev_arr(arr,i+1,n)
n = 6
arr = [5,1,8,9,4,6]
print("Initial Array:",arr)
rev_arr(arr,0,n)
print("Reversed Array:",arr)"""

"""def feb(n):
    if n<=1:
        return n
    return feb(n-1) + feb(n-2)

n = 5
print(feb(n))"""

                        # Bubble_Sort Recursion
"""
def fun(arr,i,l):
    if l == 0:
        return
    if i == l:
        l-=1
        i = 0
    if arr[i] > arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
    fun(arr,i+1,l)
arr = [2,4,100,1,12,5,6,7,50]
l = len(arr)-1
print("Initial Array:",arr)
fun(arr,0,l)
print("Sorted Array:",arr)
"""

                        # program to print subsequence by Recursive

"""def fun(arr,i,ds,n):
    if i>=n:
        print(ds)
        return
    ds.append(arr[i])
    fun(arr,i+1,ds,n)
    ds.remove(arr[i])
    fun(arr,i+1,ds,n)
arr = [3,2,1]
n = len(arr)
ds = []
fun(arr,0,ds,n)"""

                            # Subsequence with sum = k in recursion

"""def fun(arr,i,ref,l,k,ds):
    if i >= l:
        if ref == k:
            print(ds)
        return
    ds.append(arr[i])
    ref+=arr[i]
    fun(arr,i+1,ref,l,k,ds)
    ds.remove(arr[i])
    ref-=arr[i]
    fun(arr,i+1,ref,l,k,ds)
    
arr = [1,2,3,3,2,1]
l = len(arr)
k = 3
ds = []
ref = 0
fun(arr,0,ref,l,k,ds)"""


                        # to get the subsequence count whose sum = k

def fun(arr,i,ref,n,k):
    if i >= n:
        if ref == k:
            return 1
        return 0
    ref+=arr[i]
    l = fun(arr,i+1,ref,n,k)
    ref-=arr[i]
    r = fun(arr,i+1,ref,n,k)
    return l+r
arr = [1,2,3,3,2,1]
n = len(arr)
k = 3
ref = 0
print(fun(arr,0,ref,n,k))


             # To get a Permutations using freq array and Data_structure List

"""def rec_perm(arr,n,ds,freq):
    if len(ds) == n:
        print(ds)
        return
    for i in range(n):
        if freq[i] == 0:
            ds.append(arr[i])
            freq[i] = 1
            rec_perm(arr,n,ds,freq)
            ds.pop()
            freq[i] = 0
arr = [1,2,3,4,5]
n = len(arr)
ds = []
freq = [0]*n
dic = {}
rec_perm(arr,n,ds,freq)"""























































