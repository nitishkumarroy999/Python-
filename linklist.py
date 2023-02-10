class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the front of the list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print the contents of the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Create a new linked list
llist = LinkedList()

# Insert some nodes
llist.push(3)
llist.push(2)
llist.push(1)

# Print the contents of the list
llist.print_list()
