'''
Given N random numbers, sort the N in ascending order then find index of K in sorted N number list using Binary Search

[input] N: 23 87 65 12 57 32 99 81
        K: 32

[output] 2

'''

def binarySearch(N,K):
    N.sort()

    lt_pointer = 0
    rt_pointer = len(N)-1

    while lt_pointer <= rt_pointer:
        mid = (lt_pointer + rt_pointer) // 2

        if N[mid] == K:
            return mid #return value if value is matched

        elif N[mid] > K:
            rt_pointer = mid-1

        else:
            lt_pointer = mid+1

    return -1 #if not found return -1 and exit
