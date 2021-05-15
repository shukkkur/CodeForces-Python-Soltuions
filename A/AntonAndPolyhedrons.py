__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/785/A
A. Anton and Polyhedrons
'''


n = int(input())
polyhedrons = {'Tetrahedron':4, 'Cube':6,'Octahedron':8, 'Dodecahedron':12, 'Icosahedron':20}
faces = 0

for _ in range(n):
      face = input()
      faces += polyhedrons[face]

print(faces)







