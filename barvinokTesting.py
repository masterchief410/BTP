from algorithms.barvinok import barvinok
from algorithms.permanent import per
import random
import numpy as np
from math import factorial
import time
import pandas as pd

df = pd.DataFrame(columns=["N","M", "error", "timePerm", "timeBark"])

for i in range(1, 150):
    delta = 0.19
    
    N = random.randint(10, 15)
    M = random.randint(2, 4)
    A = np.random.rand(N, N)*2*delta + 1 - delta
    
    start = time.time()
    perm = per(A)
    end = time.time()
    timePerm = end - start

    start = time.time()
    estimate = barvinok(A, N, M, factorial(N))
    end = time.time()
    timeBark = end - start

    error = abs(perm-estimate)/perm
    
    df.loc[len(df.index)] = [N, M, error, timePerm, timeBark]
    print(i, N, M, error)

df.to_csv("barvinokData/delta-0-19.csv", index=False, header=True)