class CircularNode: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class CircularLinkedList: 
    def __init__(self): 
        self.head = None 
    
    def insert_at_beginning(self, data): 
        new_node = CircularNode(data) 
        if self.head is None:
            print("List is empty.")
            self.head = new_node 
            new_node.next = self.head 
        else: 
            current = self.head 
            while current.next != self.head: 
                current = current.next 
            new_node.next = self.head 
            current.next = new_node 
            self.head = new_node 
    
    def traverse(self): 
        if self.head is None: 
            print("Circular linked list is empty.") 
            return 
        current = self.head
        while True: 
            print(current.data, end=" -> " if current.next != self.head else "")
            current = current.next
            if current == self.head: 
                break 
        print(" (Back to Head)") 


cll = CircularLinkedList() 
cll.insert_at_beginning(10) 
cll.insert_at_beginning(20) 
cll.insert_at_beginning(30) 
cll.insert_at_beginning(40) 
print("Circular linked list after inserting 40,30,20, 10 at the beginning:") 
cll.traverse()

