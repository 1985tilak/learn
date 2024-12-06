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



        

my_tree = BinarySearchTree()

my_tree.insert(10)
my_tree.insert(2)
my_tree.insert(15)
print(my_tree.insert(2), "\n")

print(my_tree.contains(15))
print(my_tree.contains(2))
print(my_tree.contains(20))

# print(my_tree.root.value)
# print(my_tree.root.right.value)
# print(my_tree.root.left.value)