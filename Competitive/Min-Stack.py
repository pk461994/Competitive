"""
Design a stack that supports push, pop, top and retrieving the minimum element in constant time.
"""

class MinStack:
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.s1 = []
        self.min_stack = []

    def push(self, val):
        self.s1.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1

    def pop(self):
        if self.min_stack[-1][0] == self.s1[-1]:
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        self.s1.pop()

    def top(self):
        return self.s1[-1]

    def getMin(self):
        return self.min_stack
