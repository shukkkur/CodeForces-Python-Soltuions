__author__ = 'shukkkur'


'''
A. Maximum in Table
https://codeforces.com/problemset/problem/509/A
'''
def increase(matrix, i, j):
      return matrix[i-1][j]+matrix[i][j-1]

n = int(input())

# construct the corresponding table 
matrix = []

for i in range(1 ,n+1):
      temp = []
      for j in range(1, n+1):
            if j == 1 or i == 1:
                  temp.append(1)
            else:
                  temp.append(0)
      matrix.append(temp) 

for i in range(1, n):
      for j in range(1, n):
            matrix[i][j] = increase(matrix, i,j)

print(matrix[n-1][n-1])
            


