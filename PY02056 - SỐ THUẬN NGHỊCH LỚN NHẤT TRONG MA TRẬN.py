def isPalindrome(num):
    if num < 10:
        return False
    if str(num) != str(num)[-1::-1]:
        return False
    return True


n, m = map(int, input().split())
matrix = []
prime = -1

for i in range(n):
    matrix.append([int(i) for i in input().split()])
    for j in matrix[i]:
        if isPalindrome(j) and j > prime:
            prime = j

if prime == -1:
    print('NOT FOUND')
else:
    print(prime)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == prime:
                print(f'Vi tri [{i}][{j}]')
