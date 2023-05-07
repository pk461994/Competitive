# Stack implementation

from collections import deque
s = []
stack = deque()

print(dir(stack))
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')
print(stack)
stack.pop()
print(stack)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s1 = Stack()
s1.push(5)
s1.push(51)
s1.push(52)
s1.push(53)

# Queue implementation

q = deque()
q.appendleft(5)
q.appendleft(16)
q.appendleft(19)

print(f'Queue is {q}')
q.pop()
print(f'Queue is {q}')

class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self, val):
        self.buffer.appendleft(val)

    def pop(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
