m, n = map(int, input().split())
counter = 0
days = 0

while m > 0:
      days += 1 
      counter += 1
      if counter == n:
            m += 1
            counter = 0
      m -= 1

print(days)
