from algorithms.barvinok import barvinok
from algorithms.permanent import per
from algorithms.RAP import RAP
from algorithms.rasmussen import rasumussen
import math
import itertools
import numpy as np
import pandas as pd

N = 10
M = 3

for i in range(10000):
    A = np.round(np.random.rand(N, N))

    rasmussenEstimate = rasumussen(A, N)
    rapEstimate = RAP(A, N, 2, 3)
    numberOfOnesEstimate = math.factorial(N)*(np.count_nonzero(A)/N*N)
    barkRasmussen = -1
    barkRAP = -1
    barkNumber = -1
    if rasmussenEstimate != 0:
        barkRasmussen =  barvinok(A, N, M, rasmussenEstimate)

    if rapEstimate != 0:
        barkRAP =  barvinok(A, N, M, rapEstimate)

    if numberOfOnesEstimate != 0:
        barkNumber = barvinok(A, N, M, numberOfOnesEstimate)

    actualPerm = per(A)

    df = pd.DataFrame(columns=["N","A","Permanent","rasmussenEstimate","rapEstimate","numberOfOnesEstimate", "barkRasmussen", "barkRAP", "barkNumber"])

    df["N"] = [N]
    df["A"] = [A]
    df["Permanent"] = [actualPerm]
    df["rasmussenEstimate"] = [rasmussenEstimate]
    df["rapEstimate"] = [rapEstimate]
    df["numberOfOnesEstimate"] = [numberOfOnesEstimate]
    df["barkRasmussen"] = [barkRasmussen]
    df["barkRAP"] = [barkRAP]
    df["barkNumber"] = [barkNumber]

    df.to_csv("data/01-RAP-Rasmussen-Barvinok.csv", mode='a', index=False, header=False)
    print(i, actualPerm)