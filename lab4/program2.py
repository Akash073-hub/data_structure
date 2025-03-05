class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.head = None 
  
    def append(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head: 
            self.head = new_node 
            return 
        last = self.head 
        while last.next: 
            last = last.next 
        last.next = new_node 
  
    def delete_node(self, data): 
        current = self.head
        if current and current.data == data: 
            self.head = current.next 
            current = None 
            return

        prev = None
        while current and current.data != data: 
            prev = current 
            current = current.next
        if current is None: 
            return 
        prev.next = current.next 
        current = None 
  
    def traverse(self): 
        current = self.head 
        while current: 
            print(current.data, end=" -> " if current.next else "")
            current = current.next 
        print()

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

linked_list = LinkedList()
#append the node to LL
linked_list.append(10) 
linked_list.append(20) 
linked_list.append(45)
linked_list.traverse()
# serach key
key = 45
mal = linked_list.search(key)
print(f"Key {key} found: {mal}")
#display
linked_list.traverse()

