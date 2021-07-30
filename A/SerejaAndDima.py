__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/381/A
A. Sereja and Dima
'''


n = int(input())
cards = list(map(int, input().split()))
dima = 0
sereja = 0

turn = True

for i in range(n):
      left = cards[0]
      right = cards[-1]
      if turn:
            choice = max(left, right)
            dima += choice
            cards.pop(cards.index(choice))
            turn = False
      else:
            choice = max(left, right)
            sereja += choice
            cards.pop(cards.index(choice))
            turn = True

print(dima, sereja)
