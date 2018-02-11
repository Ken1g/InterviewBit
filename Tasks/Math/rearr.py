def arrange(A):
        for i in range(len(A)):
                A[i] += (A[A[i]] % len(A)) * len(A)
        for i in range(len(A)):
                A[i] = A[i] / len(A)

        return A

A = [4, 3, 0, 1, 2]
print(arrange(A))
