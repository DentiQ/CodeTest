s1 = input()
s2 = input()
s3 = input()


def lcs(s1, s2, s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    matrix = [[[0 for _ in range(l3+1)] for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            for k in range(1, l3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])

    return matrix[-1][-1][-1]


print(lcs(s1, s2, s3))

