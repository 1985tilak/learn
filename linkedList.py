#something like this in dict
# {
#     'value': 7
#     'next': None
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

 #print the nodes in the list.    
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

# append the node at the end of the list
    def append(self, value):  
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

# pop the node at the end of the singly linked list
    def pop(self):
        if self.head is None:
            print("empty linked_list")
            return None
        temp = self.head 
        prev = self.head
        while(temp.next):
            prev = temp 
            temp = temp.next
        self.tail = prev 
        self.tail.next = None
        self.length -= 1 
        if self.length == 0: 
            self.head = None
            self.tail = None
        return temp 
    
# prepend the node 
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1

#pop at the beginning of the list.
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1 
        if self.length == 0:
            self.tail = None
        return temp
    
#get the node at the index passed
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp
    
#set value at the index passed  (use the get method to get to the index)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True 
        return False

#insert value at the index passed
    def insert_value(self,index,value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True 
    
#remove value at the index
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop() 
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None
        self.length -= 1 
        return temp

# reverse the linked list
    def reverse(self):
        temp = self.head 
        self.head = self.tail
        self.tail = temp

        after = temp.next 
        before = None

        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp   
            temp = after 

# find the middle node in the list
    def middle_node(self):
        slow = fast = self.head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        return slow
    
    def has_loop(self):
        slow = fast = self.head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    # partition the linked list based on x such that less
    #  than x will be front of the list followed by
    #  greater than x 

    def partition_list(self, x):
        d1 = Node(0)
        p1 = d1 
        d2 = Node(0)
        p2 = d2 

        current = self.head

        while current:
            if current.value < x:
                p1.next = current 
                p1 = current 
            else:
                p2.next = current 
                p2 = current 
            current = current.next 

        p1.next = None
        p2.next = None 

        p1.next = d2.next 
        d1.next = self.head 

    # remove duplicates  using Set data type
    def remove_duplicates(self):
        prev = None
        current = self.head 
        values = set()

        while current:
            if current.value in values:
                prev.next = current.next 
                self.length -= 1
            else:
                values.add(current.value)
                prev = current
            current = current.next 







## move the fast pointer k times first.  
## and then move slow and fast at same pace and 
# return slow when fast reaches the end of list 

def find_kth_from_end(ll, k):
    slow = fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next 

    while fast:
        slow = slow.next 
        fast = fast.next 
    return slow

my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(3)
# my_linked_list.tail.next = my_linked_list.head
print(f'lenght of the list: {my_linked_list.length}')

my_linked_list.print_list()
my_linked_list.remove_duplicates()
my_linked_list.print_list()
print(f'lenght of the list after dedupe: {my_linked_list.length}')



# my_linked_list.print_list()
# my_linked_list.partition_list(6)
# my_linked_list.print_list()
# print(my_linked_list.has_loop())

# k=4
# result = find_kth_from_end(my_linked_list, k)
# print(f'kth element from end is {result.value}')

# result = my_linked_list.middle_node()
# print(result.value)

# my_linked_list.print_list()

# my_linked_list.reverse()
# print('\n')
# my_linked_list.print_list()

# my_linked_list.remove(1)
# my_linked_list.print_list()

# my_linked_list.insert_value(2, 900)
# my_linked_list.print_list()

# print(my_linked_list.get(1))
# my_linked_list.set_value(1, 100)
# my_linked_list.print_list()

# my_linked_list.prepend(0)
# my_linked_list.print_list()

# print("before pop")
# my_linked_list.print_list()

# print("\nafter pop")
# my_linked_list.pop()
# my_linked_list.print_list()

