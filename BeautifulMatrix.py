__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/263/A
'''

matrix = []
for i in range(5):
      matrix.append(list(map(int, input().split())))

for i, mat in enumerate(matrix):
      for idx, lst in enumerate(mat):
            if matrix[i][idx] == 1:
                  x1, y1 = i, idx

x2, y2 = 2,2

print(abs(x1-x2)+abs(y1-y2)) # Manhattan Distance
