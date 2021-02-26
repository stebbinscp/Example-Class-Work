def minimum_offerings(n, A):
    """Find the minimum offerigns made to each temple where
    n is the number of temples and A is an array representing their heights"""

    A_left = [0]*n
    A_right = [0]*n

    for i in range(1, n):
        if A[i] > A[i-1]: 
            A_left[i] = A_left[i-1]+1

    for i in reversed(range(n)):
        if i < n-1:
            if A[i] > A[i+1]: 
                A_right[i] = A_right[i+1]+1
    total = 0
    for i in range(n):
        total += max(A_left[i], A_right[i]) + 1
    return total

if __name__ == "__main__":
    A = [ 1, 2, 2 ]
    print(minimum_offerings(3, A))
     
    A = [ 1, 4, 3, 6, 2, 1 ]
    print(minimum_offerings(6, A))