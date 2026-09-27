class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")


    def insert_at_beginning(self, data: int):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def insert_at_end(self, data: int):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def insert_at_position(self, data: int, position: int):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position - 1):
            if not current:
                raise IndexError("Index out of bounds")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, key):
        current = self.head

        # If head needs to be deleted
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print("Value not found")
            return

        prev.next = current.next


    def delete_by_position(self,position: int):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head

        for _ in range(position -1):
            current = current.next
            if not current or not current.next:
                return
        current.next = current.next.next

    def search(self,key: int):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False    

    def length(self):
        counter = 0 
        current = self.head

        while current is not None:
            counter +=1
            current = current.next
        return counter
    
            

ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.traverse()

ll.insert_at_position(25,2)
ll.traverse()

ll.insert_at_beginning(5)

ll.traverse()

ll.delete_by_value(30)

ll.traverse()

ll.delete_by_position(100)
ll.traverse()
print(ll.search(10))

ll.traverse()

print(ll.length())
