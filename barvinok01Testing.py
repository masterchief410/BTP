from algorithms.barvinok import barvinok
from algorithms.permanent import per
import random
import numpy as np
from math import factorial
import time
import pandas as pd
import itertools

df = pd.DataFrame(columns=["N","Number of Ones","Actual Perm","Calc Perm"])
N = 2

for A in [np.reshape(np.array(i), (N, N)) for i in itertools.product([0, 1], repeat = N*N)]:
    num = np.count_nonzero(A)
    if(num == 0):
        continue
    start = time.time()
    perm = per(A)
    end = time.time()
    timePerm = end - start

    start = time.time()
    estimate = barvinok(A, N, min(N, 3), factorial(N))
    end = time.time()
    timeBark = end - start
    
    df.loc[len(df.index)] = [N, num, perm, round(estimate)]

df.to_csv("data/barvinokData/01data_n=2.csv", index=False, header=True)