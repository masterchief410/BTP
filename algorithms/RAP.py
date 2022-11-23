import numpy as np
import math
import random
# from permanent import per

def RAP(A,n,s,r):
    if n == 0:
        return 1
    else:
        W = []
        for j in range(n):
            if A[0][j] == 1:
                W.append(j)
        if len(W) == 0: 
            return 0
        else:
            k = 0
            if math.floor(math.log(n, s)) == math.ceil(math.log(n, s)):
                k = r
            else:
                k = 1
            sum = 0
            rands = []
            for i in range(k):
                j = random.randint(0, len(W)-1)
                rands.append(W[j])
            for j in rands:
                B = A 
                B = np.delete(B, 0, 0)
                B = np.delete(B, j, 1)
                sum += RAP(B, n-1, s, r)
            return len(W)*(sum/k)

# N = 6
# A = np.round(np.random.rand(N, N))
# print(A)
# print(RAP(A, N, 2, 3))
# print("Actual Permanent: ", per(A))