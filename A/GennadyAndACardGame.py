__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1097/A
A. Gennady and a Card Game
'''


on_table = list(input())
suit  = on_table[0]
rank = on_table[1]

at_hand = input().split()
can_play = False

for card in at_hand:
      if card[0] == suit or card[1] == rank:
            can_play = True
            break

print('YES') if can_play else print('NO')
