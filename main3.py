from algorithms.RAP import RAP
from algorithms.permanent import per
import numpy as np
import pandas as pd
import random
import math

M = 3
P = 0.8

for i in range(1000):
    N = random.randint(10, 15)
    A = np.where(np.random.rand(N, N)>(1-P), 1 ,0)

    actualPerm = per(A)
    if actualPerm == 0:
        print("actual Perm is 0")
        continue
    estimate = RAP(A, N, 2, 3)
    error = (estimate - actualPerm)/actualPerm
    # barkEstimate = np.array([1, math.factorial(N)*P])
    
    # flag = 0
    # while (abs(barkEstimate[-2] - barkEstimate[-1]))/actualPerm > 0.001:
    #     barkEstimate = np.append(barkEstimate, [barvinok(A, N, M, barkEstimate[-1])])
    #     if barkEstimate[-1] == 0:
    #         flag = 1
    #         print("barkEstimate becomes zero")
    #         break
    # if flag:
    #     continue
    # error = np.array([])
    # error = (barkEstimate - actualPerm)/actualPerm

    df = pd.DataFrame(columns=["N","Permanent","Error","Epochs"])
    df["N"] = [N]
    df["Permanent"] = [actualPerm]
    # df["barkEstimate"] = [barkEstimate]
    df["Error"] = [error]
    # df["Epochs"] = [np.size(error)]
    # df["A"] = [A]

    # print(A)
    df.to_csv(f"data/new01-RAP{P*100}.csv", mode='a', index=False, header=False)