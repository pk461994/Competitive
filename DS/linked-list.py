class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):             # Node to be deleted is the Head
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next       # Setting the head to next node of cur_node than making cur_node as None
            cur_node = None
            return
        # Node to be deleted is not the Head. It is somewhere in between the list
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return

        prev.next = cur_node.next       # This is if the key provided is the node with position 1
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head
        
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count+=1

        if cur_node is None:
            return print('The position was greater than the number of elements in the list')
        
        prev.next = cur_node.next       # This is if the key provided is the node with position 1
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count
    
    #Counting the items using recurssion
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.prepend("E")
# llist.insert_after_node(llist.head.next, "E")

# llist.delete_node('B')
# print('Total number of items in the list:',llist.len_iterative())

print('Total number of items using recursion in the list:',llist.len_recursive(llist.head))

llist.print_list()