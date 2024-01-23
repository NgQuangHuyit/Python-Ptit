class Matrix:
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix

    def chuyenVi(self):
        matB = [[0] * self.row for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                matB[j][i] = self.matrix[i][j]
        return Matrix(self.col, self.row, matB)

    def mul(self, mat2):
        res = [[0] * mat2.col for _ in range(self.row)]
        for r in range(self.row):
            for c in range(mat2.col):
                tmp = 0
                for i in range(self.col):
                    tmp += (self.matrix[r][i] * mat2.matrix[i][c])
                res[r][c] = tmp
        return Matrix(self.row, mat2.col, res)

    def display(self):
        for r in range(self.row):
            print(*self.matrix[r])

    def __str__(self):
        return self.matrix


for t in range(int(input())):
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append([int(num) for num in input().split()])
    a = Matrix(n, m, mat)
    b = a.chuyenVi()
    c = a.mul(b)
    c.display()
