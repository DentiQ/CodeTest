A = " " + input()
B = " " + input()

matrix = [[""]*(len(B)) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            matrix[i][j] = matrix[i-1][j-1] + A[i]
        else:
            if len(matrix[i - 1][j]) > len(matrix[i][j - 1]):
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i][j-1]

print(len(matrix[len(A)-1][len(B)-1]))
print((matrix[len(A)-1][len(B)-1]))


