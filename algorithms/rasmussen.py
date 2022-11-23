import numpy as np
import random

def rasumussen(A,n):
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
            j = random.randint(0, len(W)-1)
            j = W[j]
            B = A 
            B = np.delete(B, 0, 0)
            B = np.delete(B, j, 1)
            return len(W)*rasumussen(B, n-1)



