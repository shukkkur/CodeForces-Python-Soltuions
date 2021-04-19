numCases = int(input())
total = 0
for _ in range(numCases):
      x, y, z = map(int, input().split())

      if (x+y+z > 1):
            total += 1
            
print(total)
