import numpy as np
import itertools
import math


def barvinok(A, N, M, base):
    f = np.zeros(M+1)
    g = np.zeros(M+1)

    tempPerm = np.array(range(1, N+1))
    
    g[0] = base
    num = pow((base / math.factorial(N)), (1/N))

    for k in range(1, M+1):
        all = list(itertools.combinations(tempPerm, k))
        allCombinations = [all,all]
        allProd = list(itertools.product(*allCombinations))

        for each in allProd:
            prod = 1.
            for i in range(0, k):
                prod = prod * (A[each[0][i]-1][each[1][i]-1]-num) 
            g[k] = g[k] + prod * pow(num, N-k)
        g[k] = g[k] * math.factorial(N-k)

    # g[k] = sigma(j=0:k-1) (k-1Cj)*(g[j])*(f[k-j])
    # f[k] = (g[k] - sigma(j=1:k-1) k-1Cj * g[j] * f[k-j])/g[0]*k-1

    f[0] = math.log(g[0])

    for k in range(1, M+1):
        sigma = 0
        for j in range(1, k):
            sigma = sigma + math.comb(k-1, j)*g[j]*f[k-j]
        f[k] = (g[k] - sigma)/g[0]

    ans = f[0]

    for i in range(1, M+1):
        ans = ans + (f[i]/(math.factorial(i)))
    calculatedPerm = math.exp(ans)

    return calculatedPerm