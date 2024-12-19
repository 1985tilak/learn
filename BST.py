class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True 
        temp = self.root 
        while (True):
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left 
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True 
                temp = temp.right

    def contains(self, value):
        # if self.root == None:  No need to check if tree is empty
        #     return False      since while loop will break if temp is None. 
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right
            else:
                return True 
        return False 
    
    # recursive contains 
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_contains(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_contains(self.root, value)


    
        



        

my_tree = BinarySearchTree()

my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print('Root', my_tree.root.value)
print('Root -> left', my_tree.root.left)
print('Root -> right', my_tree.root.right)



# print(my_tree.r_contains(15))
# print(my_tree.r_contains(2))
# print(my_tree.r_contains(20))

# print(my_tree.root.value)
# print(my_tree.root.right.value)
# print(my_tree.root.left.value)