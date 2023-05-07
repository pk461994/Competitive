class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        """
        Our node has three properties, a piece of data, a pointer to next node and to the previous node
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList(object):
    def __init__(self, head=None):
        # Set the head. Head being the first node in list
        self.head = head

    def traverse(self):
        # Grab the first node
        curr_node = self.head

        # Keep going until you reach the end of the list.
        while curr_node is not None:
            # Print data and grab the node
            print(curr_node.data)
            curr_node = curr_node.next_node

    def get_list_size(self):
        # Define incrementer
        count = 0
        # Grab first node
        curr_node = self.head
        # Keep going until you reach the end of the list.
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next_node
        return count

    def insert_beg(self, data):

        # Define a new node
        new_node = Node(data)

        # Take the new node and Set the next node equal to the old head
        new_node.next_node = self.head

        # Because it's the head, the previous point of the new_node will be nothing
        new_node.prev_node = None

        # Handle the non-empty list case and assign prev_node of head(Now on 2nd position) to the new_node
        if self.head is not None:
            self.head.prev_node = new_node

        # Update the head to the new_node
        self.head = new_node

    def insert_end(self, data):
        # Define new Node
        new_node = Node(data)
        # At the end of our list, next pointer points to nething
        new_node.next_node = None

        # Handle empty list
        if self.head == None:
            new_node.prev_node = None # As the inserted node is at beginning
            self.head = new_node
            return

        # If the list isn't empty. First grab the first node
        first_node = self.head

        # Go to the end of our list
        while first_node.next_node:
            first_node = first_node.next_node

        # When it reaches to end set the next node to the New Node to be inserted at end
        first_node.next_node = new_node
        new_node.prev_node = first_node


    def insert_before(self, ref_node, data):
        if self.head is None:
            print('The node is empty')
            return

        # Define a new node
        new_node = Node(data)

        new_node.prev_node = ref_node.prev_node
        ref_node.prev_node = new_node
        new_node.next_node = ref_node

        # If previous node is not None

        if new_node.prev_node is not None:
            new_node.prev_node.next_node = new_node
        else:
            self.head = new_node

    def insert_after(self, ref_node, data):
        if self.head is None:
            print('List is empty')
            return

        # Define a new node
        new_node = Node(data)

        # New node next pointer will be the reference node next pointer
        new_node.next_node = ref_node.next_node
        ref_node.next_node = new_node
        new_node.prev_node = ref_node

        if new_node.next_node is not None:
            new_node.next_node.prev_node = new_node

    def reverse_list(self):
        # Define 2 nodes, the first Node and the second node
        # p_node will be the first node that need to be changed to last node
        p_node = self.head
        q_node = p_node.next_node  # q_node is the 2nd node after p_node

        p_node.next_node = None  # Making p_node as last node as after that it will be None
        p_node.prev_node = q_node

        # Keep going till the end
        while q_node is not None:
            q_node.prev_node = q_node.next_node
            q_node.next_node = p_node
            p_node = q_node
            q_node = q_node.prev_node

        # Redefine head
        self.head = p_node

    def delete_at_start(self):
        if self.head is None:
            print('List is empty')
            return

        # If only a head is present in list
        if self.head.next_node is None:
            self.head = None
            return

        # Assign the head equal to the node after the head
        self.head = self.head.next_node
        self.head.prev_node = None

    def delete_at_end(self):
        if self.head is None:
            print('List is empty')
            return

        # If only a head is present in list
        if self.head.next_node is None:
            self.head = None
            return

        # Grab the first node
        curr = self.head
        while curr.next_node is not None:
            curr = curr.next_node
        curr.prev_node.next_node = None

    def remove_duplicates(self):

        # Grab the first node and the second node
        previousNode = self.head
        currentNode = self.head.next_node

        if self.head is None:
            print('List is empty')
            return

        keys = set([previousNode.data])
        while currentNode:
            data = currentNode.data
            if data in keys:
                previousNode.next_node = currentNode.next_node

                if previousNode.next_node != None:
                    previousNode.next_node.prev_node = previousNode
                currentNode = currentNode.next_node

            else:
                # If it's not duplicate
                keys.add(data)
                previousNode = currentNode
                currentNode = currentNode.next_node

    def delete_element_by_value(self, x):
        if self.head is None:
            print('No element to delete, List is empty')
            return

        if self.head.next_node is None:
            if self.head.data == x:
                self.head = None
            else:
                print('Item not found')
            return

        if self.head.data == x:
            self.head = self.head.next_node
            self.head.prev_node = None
            return

        # Grab the first node
        n = self.head

        # Traverse list
        while n.next_node is not None:
            # If the value matches
            if n.data == x:
                break
            n = n.next_node

            if n.next_node is not None:
                # Take the one we're currently on, grab it and grab the next pointer and point it to element comes after the ones matches basically
                n.prev_node.next_node = n.next_node
                n.next_node.prev_node = n.prev_node

# ===============================Class Execution======================================== #
double_list = DoublyLinkedList()
double_list.insert_beg(90)
double_list.insert_beg(91)
double_list.insert_beg(92)
double_list.insert_beg(90)
double_list.insert_beg(91)

print('-'*100)
print('After insertion')
double_list.traverse()

# Define a reference node
first_node = double_list.head

# Insert before that node
double_list.insert_before(first_node, 50)

print('-'*100)
print('After insertion Before')
double_list.traverse()

# Insert before that node
double_list.insert_end(100)

print('-'*100)
print('After insertion at end')
double_list.traverse()

# Define a reference node
second_node = double_list.head.next_node
# Insert after that node
double_list.insert_after(second_node, 70)
double_list.insert_after(second_node, 72)

print('-'*100)
print('After insertion After')
double_list.traverse()

# Reverse the list
double_list.reverse_list()

print('-'*100)
print('After list reversal')
double_list.traverse()

# Delete at start
# double_list.delete_at_start()
#
# print('-'*100)
# print('After head deletion')
# double_list.traverse()

# Delete at end
# double_list.delete_at_end()
#
# print('-'*100)
# print('After tail deletion')
# double_list.traverse()

# Reverse the list
double_list.remove_duplicates()

print('-'*100)
print('After removing duplicates')
double_list.traverse()
