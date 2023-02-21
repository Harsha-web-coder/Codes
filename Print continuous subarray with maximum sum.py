import sys
def kadane(A):
    if len(A) <= 1:
        return A
    maxSoFar = -sys.maxsize
    maxEndingHere = 0
    start = 0
    end = 0
    beg = 0
    for i in range(len(A)):
        maxEndingHere = maxEndingHere + A[i]
        if maxEndingHere < A[i]:
            maxEndingHere = A[i]
            beg = i
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i
    print("The contiguous sublist with the largest sum is", A[start: end + 1])
 
 
if __name__ == '__main__':
 
    A = [-2,-3,4,-1,-2,1,5,-3]
    kadane(A)
