class Solution:
    def repeatedNumber(self, A):
        xr = 0
        for i in range(len(A)) :
            xr ^= A[i]
            xr ^= (i+1)
        bitNo = 0
        while True :
            if ((1<<bitNo) & xr) != 0 :
                break 
            bitNo += 1
        one, zero = 0, 0
        for i in range(len(A)) :
            if (1<<bitNo)&A[i] != 0 :
                one ^= A[i]
            else :
                zero ^= A[i]
            if (1<<bitNo)&(i+1) != 0 :
                one ^= (i+1)
            else :
                zero ^= (i+1)
        c = 0
        for i in range(len(A)) :
            if A[i] == one :
                c += 1
            if c == 2 :
                return [one, zero] 
        return [zero, one]
''' bit manupulation solution : time O(N), space O(1) '''




def missingAndRepeating(arr, n):
    s1, s2, sn1, sn2 = 0, 0, 0 ,0 
    for i in range(n) :
        s1 += arr[i]
        s2 += arr[i] * arr[i]
    sn1 = (n*(n+1))// 2
    sn2 = ((n)*(n+1)*(2*n+1))// 6
    val1 = s1-sn1 
    val2 = s2-sn2
    val2 = val2//val1
    x = (val1+val2)//2
    y = (val2-x)
    return [y, x]
''' time O(N), space O(1) '''


def missingAndRepeating(arr, n):
    rep, mis = -1, -1
    a = [-1] * (n+1)
    for i in arr :
        a[i] += 1
    for i in range(1,n+2) :
        if a[i] == 1 :
            rep = i 
        elif a[i] == -1 :
            mis = i
        if rep != -1 and mis != -1 :
            return [mis, rep]
''' time O(N), space O(N) '''

def missingAndRepeating(arr, n):
    for i in range(1, n+1) :
        c = 0
        for j in range(len(arr)) :
            if arr[j] == i :
                c += 1
        if c == 2 :
            rep = i
        elif c == 0 :
            mis = i
    return [mis, rep]
''' time O(N^2), space O(1) '''
