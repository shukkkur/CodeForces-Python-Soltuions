__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/706/B
B. Interesting drink
'''

def binSearch(arr, i):
      low = 0
      high = len(arr) - 1

      if i < arr[0]:
            return 0
      elif i >= arr[high]:
            return high + 1
      
      while low != high:
            mid = int((low + high) / 2)

            if (arr[mid] == i and arr[mid + 1]) > i or (i > arr[mid] and i < arr[mid + 1]):
                  return mid + 1
            elif arr[mid] <= i:
                  low = mid
            else:
                  high = mid
      return low


n = int(input())
prices = list(map(int, input().split()))
q = int(input())
coins  = []

for coin in range(q):
      coins.append(int(input()))

prices.sort()

for coin in coins:
      print(binSearch(prices, coin))
