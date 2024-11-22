from collections import deque

queue = deque()

words= input()
words = words.split()

for w in words:
    queue.appendleft(w)
 
print(queue)

for w in words:
    owords = queue.pop()
    if "o" in owords:
        print(owords)