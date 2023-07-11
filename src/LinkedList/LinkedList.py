class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            
            current_node.next = Node(data)
    
    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(3)
    linked_list.insert(5)
    linked_list.insert(7)

    linked_list.display()
