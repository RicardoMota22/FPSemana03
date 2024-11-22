from collections import deque

stack = deque()

num = input()
num = num.split()

for n in num:
    stack.append(int(n))
 
print(stack)

for n in num:
    sqaures = stack.pop()
    print(sqaures*sqaures)



    


