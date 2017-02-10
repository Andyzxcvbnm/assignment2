def max_subarray(A):
    a = b = A[0]
    for x in A[1:]:
        a = max(0, a + x)
        b = max(b, a)
    return b
