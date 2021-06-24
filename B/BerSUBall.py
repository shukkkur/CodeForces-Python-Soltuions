__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/489/B
B. BerSU Ball
'''


n = int(input())
boys = sorted(list(map(int, input().split())))
m = int(input())
girls = sorted(list(map(int, input().split())))
pairs = 0

for boy in boys:
      for girl in girls:
            if boy == girl:
                  pairs += 1
                  girls.remove(boy)
                  break
                  
            elif (boy + 1) == girl:
                  pairs += 1
                  girls.remove(boy+1)
                  break
                  
            elif (boy - 1) == girl:
                  pairs += 1
                  girls.remove(boy-1)
                  break
            
print(pairs)      
      

      
