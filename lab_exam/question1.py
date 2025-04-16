class circularNode:
    def __init__(self,data):
        self.data=data
        self.next=None
		
class circularLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data): 
        new_node=circularNode(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                temp.next = new_node
                new_node.next = self.head
                self.head = new_node
    def delete_node(self):
        if self.head is None:
            print("empty circular node")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next

    def display(self):
        if self.head is None:
            print("Circular list is empty")
        else:
            temp = self.head
            print("Circular List:", end=" ")
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()

c=circularLinkedList()
c.insert_at_beginning(10)
c.insert_at_beginning(30)
c.insert_at_beginning(20)
c.delete_node()
c.display()
