#A linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#LinkedList is collection of nodes. Create head and insert nodes into it
class Linkedlist:
    def __init__(self):
        self.head = None  #Create empty LinkedlIst

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  #Create node using data.
        self.head = node

    def print_out(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next  #Shifting head to next node
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next #Shifting node to next to next... So that the next will automatically be cut off
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            # self.insert_at_beginning(data)

if __name__ == '__main__':
    root = Linkedlist()
    # root.insert_at_beginning(5)
    # root.insert_at_beginning(10)
    # root.insert_at_beginning(15)
    root.insert_at_end(567)
    root.insert_at_end(99)
    root.insert_at_end(108)
    root.insert_at(2, 1000)
    root.insert_at(1, 40)
    root.print_out()
    root.remove_at(3)
    root.remove_at(1)

    root.insert_values(['banana', 'mango', 'grapes'])
    root.print_out()
