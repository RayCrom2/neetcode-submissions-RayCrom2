class MinHeap:

    
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def bubble_up(self, index: int) -> None:
            parent_idx = index // 2
            while index > 1 and self.heap[index] < self.heap[parent_idx]:
                if self.heap[index] < self.heap[parent_idx]:
                    self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                else:
                    return
                index, parent_idx = parent_idx, (parent_idx // 2)
            

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.bubble_up(self.size + 1)
        self.size = self.size + 1


    def bubble_down(self, index: int) -> None:
        child = 2 * index  # left child
        while child <= self.size:
            if child + 1 <= self.size and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[child] >= self.heap[index]:
                break

            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index  # left child
            

    def pop(self) -> int:
        if self.size == 0:
            return -1
        return_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size = self.size - 1
        self.bubble_down(1)
        return return_value
        
        
        

    def top(self) -> int:
        if self.size == 0:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        self.size = len(nums)
        for i in range (self.size // 2, 0, -1):
            self.bubble_down(i)
      