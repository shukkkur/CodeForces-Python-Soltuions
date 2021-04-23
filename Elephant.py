__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/617/A
'''


x = int(input())
steps = [5,4,3,2,1]
count = 0

while x != 0:  # 12
      if x in steps:
            count += 1
            break
      else:
            if x > steps[0]:
                  x = x - steps[0]
                  count += 1
                  if x < steps[0]:
                        steps.pop(0)
print(count)







