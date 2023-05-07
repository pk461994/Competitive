# Defining node object
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList(object):
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def insert_at_front(self, data):
        # Define new node
        new_node = Node(data)

        # Set the second node to equal the old first one. So the current head will become the 2nd node as we have new node
        new_node.set_next_node(self.head)

        # Reset the head to the new node
        self.head = new_node

    def insert_at_end(self, data):
        # Define a new node
        new_node = Node(data)
        head_node = self.head

        # If there isn't a head node then that is the last node
        if head_node is None:
            head_node = new_node
            return
        # Otherwise let's find last node
        last_node = head_node

        # As long as there is next node it means we haven't reached the end
        while last_node.get_next_node() != None:
            last_node = last_node.get_next_node()

        # When we reach the end set the node
        last_node.set_next_node(new_node)
        # We've reached the end so defined that as new node
        self.end = new_node

    def insert_middle(self, middle_node, data):
        if middle_node is None:
            print("The node you selected doesn't exist")
        new_node = Node(data)
        '''
        Get the middle node, then get the node after it and set it to the new node
        Using middle_node.get_next_node() we can get next node of middle_node i.e, 35
        After that we set that (35) as the next node to the new_node(50) we want to enter
        Then we need to set new_node(50) as the next node to the middle node(55)
        '''
        new_node.set_next_node(middle_node.get_next_node())
        middle_node.set_next_node(new_node)

    def traverse(self):
        # define a node
        node = self.head
        while node is not None:
            print(node.get_data())
            node = node.get_next_node()

    def list_size(self):
        current_node = self.head
        current_count = 0
        while current_node:
            current_count += 1
            current_node = current_node.get_next_node()
        return current_count

    def delete_node(self, value):
        # Define current node as the beginning node
        current_node = self.head
        found = False
        previous_node = None

        if current_node is None:   # Means the list is empty
            return
        '''
        If current_node is not None and we haven't got the value on current node we'll shift further
        By assigning current_node to previous_node and current_node as the next node that comes after current_node
        '''
        while current_node is not None and found is False:
            if current_node.data == value:
                found = True
                break
            else:
                previous_node = current_node
                current_node = current_node.get_next_node()
        if current_node is None:
            raise ValueError("Data not in list!!!")

        '''
        If previous_node is None we'll get next node of the previous node else we'll 
        Get the next node of current_node and set that node as next_node to previous_node
        like nodes are 1, 2, 3, 4
        As 1st node is not none(value is 1) so we'll make previous node as 2 and current_node will be 3
        '''
        if previous_node is None:
            # If it was None then set the new head equals to the node after the old head
            self.head = current_node.get_next_node()
        else:
            # Otherwise take the previous node and set the node after it to be the one that contains the value and comes after it
            previous_node.set_next_node(current_node.get_next_node())

    def search_list(self, value):
        current_node = self.head
        result_list = []

        if current_node is None:
            return
        while current_node is not None:
            if current_node.data == value:
                result_list.append(current_node)
                current_node = current_node.get_next_node()
            else:
                current_node = current_node.get_next_node()
        return result_list

    def delete_list(self):
        # Start from the beginning
        current_node = self.head
        while current_node:
            # Grab next node
            next_node = current_node.next_node

            # Delete the current node
            del current_node.data

            # Set current node equals to the next node
            current_node = next_node

    def remove_duplicates(self):
        # Grab the first node and the node after the first
        previous_node = self.head
        currentNode = previous_node.next_node

        # Build a set to store non duplicate values
        keys = set([previous_node.data])

        while currentNode:
            data = currentNode.data

            # If it is a duplicate
            if data in keys:
                previous_node.next_node = currentNode.next_node
                currentNode = currentNode.next_node
            else:
                keys.add(data)
                # Reassign the nodes
                previous_node = currentNode
                currentNode = currentNode.next_node

    def kth_to_last(self, k):
        # print from some index(k) till the last of linkedlist
        # If k is negative return nothing
        if k < 0:
            return None
        # If k is 0 then print the list
        if k == 0:
            self.traverse()
            return

        # Grab the list length
        list_length = self.list_size()

        if k > list_length:
            print('You chose a k that is longer than the list')

        # Start from the beginning
        p1 = self.head

        for i in range(1, list_length+1):
            if i >= k:
                print(p1.data)
                p1 = p1.next_node
            else:
                p1 = p1.next_node

    def sum_linked_list(self, linked_list):
        total = 0
        p1 = self.head
        p2 = linked_list.head

        # Loop through each linked list
        while p1:
            if isinstance(p1.data, (int, float)):
                total = total + p1.data
                p1 = p1.next_node
            else:
                p1 = p1.next_node

        while p2:
            if isinstance(p2.data, (int, float)):
                total = total + p2.data
                p2 = p2.next_node
            else:
                p2 = p2.next_node
        return total


linked_list = LinkedList()
linked_list2 = LinkedList()

linked_list2.insert_at_front(1001)
linked_list2.insert_at_front(1002)
linked_list2.insert_at_front(1018)

linked_list.insert_at_front(35)
linked_list.insert_at_front(108)
linked_list.insert_at_front(108)
linked_list.insert_at_front(55)
linked_list.insert_at_front(45)

linked_list.insert_at_end(90)

second_node = linked_list.head.get_next_node()
linked_list.insert_middle(second_node, 50)
linked_list.traverse()

# print('Before deletion', linked_list.list_size())
# linked_list.delete_node(90)
# print('After deletion', linked_list.list_size())

print(linked_list.search_list(108))

# linked_list.delete_list()
# try:
#     print(linked_list.head.data)
# except Exception as e:
#     print(e)

linked_list.remove_duplicates()
print('-'*50)
linked_list.traverse()
print('-'*50)

linked_list.kth_to_last(4)
print('-'*50)
print('After adding linked lists')
print(linked_list.sum_linked_list(linked_list2))
