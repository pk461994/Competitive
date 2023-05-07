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

double_list = DoublyLinkedList()
double_list.insert_beg(90)
double_list.insert_beg(91)
double_list.insert_beg(92)

print('-'*100)
print('After insertion')
double_list.traverse()
