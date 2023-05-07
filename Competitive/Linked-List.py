class Node:
    """
    Node will contain Data and the next pointer.
    """
    def __init__(self, data=None, next_pointer=None):
        self.data = data
        self.next_pointer = next_pointer

class LinkedList:
    """
    LinkedList contains head. Define head as None and LinkedList will be created
    We'll insert nodes
    """
    def __init__(self):
        self.head = None

    def insert_node_at_beginning(self, data):
        # Create the node using the data. We've to make the new element as head
        node = Node(data, self.head)
        self.head = node    # Assign head to the node as it's the first Node

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''     # To remove --> from the end of print
            if itr.next_pointer:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next_pointer
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next_pointer
        return count

    def insert_node_at_end(self, data):
        # If we want to insert at end in empty LinkedList, then create Node at current head which is None before insertion
        if self.head is None:
            self.head = Node(data, None)
            return

        # If LinkedList is not none and contains Nodes
        itr = self.head
        while itr.next_pointer:     # Stop head before last node as last node's pointer will be None
            itr = itr.next_pointer
        itr.next_pointer = Node(data)   # Once we reach last we will create a node with the data

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_node_at_beginning(data)
            return

        # If index is valid and somewhere in the LinkedList
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next_pointer)
                itr.next_pointer = node   # The next node will be current node as we inserted fresh node in current node position
                break             # Break because the element has been inserted no further execution required
            itr = itr.next_pointer
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next_pointer  # If we want to remove 1st index Node shift the head to next node
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                # The next index of itr will be next to next of node
                itr.next_pointer = itr.next_pointer.next_pointer  # To shift the index to next to next node
                break
            itr = itr.next_pointer
            count += 1

root = LinkedList()
root.insert_node_at_beginning(5)
root.insert_node_at_beginning(10)
root.insert_node_at_beginning(15)

root.insert_at(2, 567)

root.insert_node_at_end(100)
root.insert_node_at_end(101)

root.insert_at(1, 40)

root.print()

root.remove_at(3)

root.print()

root.remove_at(0)

root.print()
print(root.get_length())
