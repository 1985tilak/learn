class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key): # __ at the beginning means private method
        my_hash = 0 
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

# def item_in_common(list1, list2):  ## this is O(n2) - nested loops inefficient
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True 
#     return False 

def item_in_common(list1, list2):  # this is O(n + n) 
    my_dict = {}                   #   O(2n) = O(n)  efficient way 
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True 
    
    return False 


def find_duplicates(nums):
    num_count = {}
    for num in nums:  # O(n)
        num_count[num] = num_count.get(num, 0) + 1 
    
   
    duplicates = []
    for num, count in num_count.items(): # O(n)
        if count > 1:
            duplicates.append(num)

    return duplicates

## O(n) + O(n) = O(2n) = O(n)
def first_non_repeating_char(string):
    char_count = {}

    for char in string:  ## O(n)
        char_count[char] = char_count.get(char, 0) + 1 
    
    for char in string:  ## O(n)
        if char_count[char] == 1:
            return char
        
    return None


## O(n) * O(k log k) = O(n * k log k)
def group_anagrams(strings):
    anagrams = {}
    for string in strings:   # O(n)
        sorted_string = ''.join(sorted(string))  # O(k log k)
        
        if sorted_string in anagrams:  # O(1)
            anagrams[sorted_string].append(string)
            print("if string present : ", anagrams)
        else:
            anagrams[sorted_string] = [string]
            print("if string NOT present :   ", anagrams)
    return list(anagrams.values())

## overall O(n)
def two_sum(nums, target):
    nums_index = {}

    for index, num in enumerate(nums):  # O(n)

        complement = target - num 

        if complement in nums_index:  # O(1)
            return [nums_index[complement], index]
        
        nums_index[num] = index 
    
    return []


# overall O(n)
def subarray_sum(nums, target):
    cumulutive_sum = {0: -1}  # initialize to 0: -1 to handle if the target is the first element
                              # also called "prefix sum" technique. 
                              # this also simplifies the for loop 
                              # no need of  "if block"
    current_sum = 0 

    for i, num in enumerate(nums):
        current_sum += num 

        # if current_sum == target:
        #     return[0, i]
        
        if (current_sum - target) in cumulutive_sum:
            return [cumulutive_sum[current_sum - target] + 1, i]
        
        cumulutive_sum[current_sum] = i 
    
    return []


def remove_duplicates(my_list):
    #use set() - convert the input list to set and back to list. 
    # set will only hold unique values  But the order might not be preserved. 

    new_list = list(set(my_list))
    return new_list



def remove_duplicates_preserve_order(my_list):
    seen = set()
    new_list = []

    for item in my_list:

        if item not in seen:
            new_list.append(item)
            seen.add(item)
    return new_list

def has_unique_chars(string):
    seen = set()

    for char in string:
        if char in seen:
            return False
        
        seen.add(char)
    
    return True 

def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    
    pairs = []
    
    for num in arr2:
        if (target - num) in set1:
            pairs.append(((target - num), num))
    return pairs

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0 

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num 
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1 
                current_length += 1

            longest = max(longest, current_length)

    return longest


nums = [100,2,345,123,1,3,4]

print(longest_consecutive_sequence(nums))
    

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# target = 7
# print(find_pairs(arr1, arr2, target))       



# string = "abcdefg"
# print(has_unique_chars(string))

# my_list = [1,1,1,2,2,3,4,5,5,5,6,89]
# print(remove_duplicates_preserve_order(my_list))

# my_list = [1,1,1,2,2,3,4,5,5,5,6,89]
# print(remove_duplicates(my_list))


# nums = [1,2,3,4,5]
# target = 6
# print(subarray_sum(nums, target)) 
# print(two_sum(nums, target))


# strings = ["tea", "eat", "tan", "nat"]
# print(group_anagrams(strings))

# string = "ttiillaakk"
# print(first_non_repeating_char(string))


# nums = [1,2,3,4,4,4,5,6,7,7]
# print(find_duplicates(nums))


# list1 = [2,3,4,5]
# list2 = [6,7,8,9]

# print(item_in_common(list1, list2))

# my_hash_table = HashTable()
# my_hash_table.set_item("bolts", 1400)
# my_hash_table.set_item("lumber", 14)


# print(my_hash_table.get_item("bolts"))
# print(my_hash_table.get_item("lumber"))
# print(my_hash_table.get_item("nuts"))

# print(my_hash_table.keys())


# my_hash_table.print_table()