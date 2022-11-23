from algorithms.barvinok import barvinok
from algorithms.permanent import per
import numpy as np
import pandas as pd
import random

M = 3

for i in range(10000):
    N = random.randint(10, 15)
    A = np.where(np.random.rand(N, N) > 0.3, 1, 0)

    actualPerm = per(A)
    if actualPerm == 0:
        continue
    
    # [-0.8, 0.4)
    preError = 0.4*random.random() - 0.8
    preErrorEstimate = actualPerm * (1+preError)

    barkEstimate = barvinok(A, N, M, preErrorEstimate)
    error = (barkEstimate - actualPerm)/actualPerm

    df = pd.DataFrame(columns=["N","Permanent","barkEstimate","PreError","Error"])
    df["N"] = [N]
    df["Permanent"] = [actualPerm]
    df["PreError"] = [preError]
    df["barkEstimate"] = [barkEstimate]
    df["Error"] = error

    df.to_csv("data/01-PreError-Barvinok.csv", mode='a', index=False, header=False)