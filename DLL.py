class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        return True 
    
    def pop(self):
        if self.length == 0:
            print("empty list!")
            return None
        temp = self.tail 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None 
        self.length -= 1 
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1 
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            
        self.length -= 1 
        return temp
    

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:  # if the index is in first half of list, start from head 
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else: # if index in 2nd half of list, start from tail
            temp = self.tail 
            for _ in range(self.length-1, index, -1):
                temp = temp.prev 
        return temp 
    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False 
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next 
        new_node.prev = before
        new_node.next = after 
        before.next = new_node
        after.prev = new_node
        self.length += 1 
        return True 


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0: 
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev 
        after = temp.next 

        before.next = after
        after.prev = before 

        temp.next = None
        temp.prev = None

        self.length -= 1 
        return temp 
    

        



        
        
    


        
        
        
myDLL = DoublyLinkedList(7)
myDLL.append(10)
myDLL.append(11)
myDLL.append(12)
myDLL.append(13)


myDLL.remove(5)

# myDLL.insert(3,20)
# print(myDLL.set_value(2,3))
myDLL.print_list()

# print(myDLL.get(4).value)

# print(myDLL.pop_first())
# print(myDLL.pop_first())
# print(myDLL.pop_first())
# print(myDLL.pop_first())


# myDLL.print_list()

# myDLL.prepend(21)
# myDLL.print_list()


# print(myDLL.pop().value)
# print(myDLL.pop().value)    
# print(myDLL.pop().value)
# print(myDLL.pop())
# myDLL.print_list()
        
        
