A = [2, 1, 5, 3, 4]


def slideWindow(A, k=3):
    S1 = sum(A[0:k])
    n = len(A)
    M = S1
    # Sₗ₊₁ = Sₗ - A[l] + A[l+k]
    for left in range(n - k):
        S1 = S1 - A[left] + A[left + k]
        M = max(M, S1)

    print(M)


slideWindow(A)
