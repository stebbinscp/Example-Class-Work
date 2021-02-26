import random
import math

def partition(A, p, r):
    """
    Partition function to split based on the random pivot element
    """
    pivot = random.randint(p,r)
    A[pivot], A[r] = A[r], A[pivot]
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i+1

def randomizedqs(A,p,r):
    """
    Run randomized quick-sort
    """
    if p < r:
        q = partition(A, p, r)
        randomizedqs(A, p, q-1)
        randomizedqs(A, q+1, r)


A = [1,6,2,7,9,9,2,4,1]
randomizedqs(A, 0, len(A)-1)
print(A)