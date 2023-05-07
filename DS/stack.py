class Stack():
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):     #To know whether stack is empty or not
        return self.items== []

    def peek(self):         #To return the top item in the stack
        if not self.is_empty():
            # return self.items[-1]
            return print('The top item in stack is:',self.items[-1])      

    def get_stack(self):
        return self.items

s = Stack()
s.push('A')
s.push('B')
s.push('C')
print(s.get_stack())
s.push('D')
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())

'''
Reverse string using Stack
'''
def reverse_string(stack, input_str):
    # Loop through string and push contents character by character onto stack
    for i in range(len(input_str)):
        stack.push(input_str[i])
    
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str
stack = Stack()
input_str = 'This is Prashant'
print('Reversed string is:',reverse_string(stack, input_str))



'''
Stack DS to conver integer values to binary
Example: 242
242/2 = 121 ->1
121/2 = 60  ->1
60/2  =30   ->0
30/2  =15   ->0
15/2  =7    ->1
7/2   =3    ->1
3/2   =1    ->1
1/2   =0    ->1

So, int(11110011, 2) will give us output of 242
'''

from stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_2(242))






