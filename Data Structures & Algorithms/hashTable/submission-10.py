class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        index = self.get_index(key)
        if not self.table[index]:
            self.table[index] = newNode
            self.size = self.size + 1
        else:
            curr = self.table[index]
            while(curr.next):
                if curr.key == key:
                    curr.value = value
                    return
                curr = curr.next
            if curr.key == key:
                curr.value = value
            else:
                curr.next = newNode
                self.size = self.size + 1
                
        
        if self.size >= (self.capacity // 2):
            self.resize()


    def get(self, key: int) -> int:
        index = self.get_index(key)
        if self.table[index]:
            curr = self.table[index]
            while curr:
                if curr.key == key:
                    return curr.value
                curr = curr.next
        return -1
            

    def remove(self, key: int) -> bool:
        index = self.get_index(key)
        curr = self.table[index]
        
        if curr and curr.key == key:
            self.table[index] = curr.next
            self.size = self.size - 1
            return True
        
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size = self.size - 1
                return True
            curr = curr.next
        return False
        
                 

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        newTableCapacity = self.capacity * 2
        newTable = HashTable(newTableCapacity)
        for i in range(self.capacity):
            curr = self.table[i]
            while curr:
                newTable.insert(curr.key, curr.value)
                curr = curr.next
        self.table = newTable.table
        self.capacity = newTable.capacity
        self.size = newTable.size

    def get_index(self, key) -> int:
        return hash(key) % self.capacity;
