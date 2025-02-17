class MaxHeap:
    def __init__(self):
        self.heap =[]

    def _left_child(self, index):
        return 2 * index + 1 
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2 
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _sink_down(self, index):
        max_index = index
        while True:
                left_index = self._left_child(index)
                right_index = self._right_child(index)

                if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                    max_index = left_index

                if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                    max_index = right_index

                if max_index != index:
                    self._swap(max_index, index)
                    index = max_index
                else: 
                    return 
             
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
    

def find_kth_smallest(nums, k):
    max_heap = MaxHeap()

    for num in nums:
        max_heap.insert(num)

        if len(max_heap.heap) > k:
            max_heap.remove()

    return max_heap.remove()

def streams_max(nums):
    max_heap = MaxHeap()
    max_stream = []

    for num in nums:
        max_heap.insert(num)
        max_stream.append(max_heap.heap[0])

    return max_stream


  
nums  = [7,3,4,5,45]
print(streams_max(nums))


# nums = [1,1,27,3,4,5,6,77,7]
# k = 3 
# print(find_kth_smallest(nums, k))

# myHeap = MaxHeap()

# myHeap.insert(95)
# myHeap.insert(75)
# myHeap.insert(80)
# myHeap.insert(55)
# myHeap.insert(60)
# myHeap.insert(50)
# myHeap.insert(65)

# print(myHeap.heap)

# myHeap.remove()

# print(myHeap.heap)

# myHeap.remove()

# print(myHeap.heap)

