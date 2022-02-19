class DLLNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head, self.tail = DLLNode(-1, -1), DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def prepend(self, node) -> None:
        
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next = node
        node.next.prev = node
    
    def pop(self, node=None) -> DLLNode:
        if self.tail.prev == self.head:
            return None
        
        if not node:
            node = self.tail.prev
        
        node.next.prev = node.prev
        node.prev.next = node.next
        return node
    
    def update(self, node):
        self.pop(node)
        self.prepend(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.lru_dll = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.lru_dll.update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.lru_dll.update(node)
            return
        
        if len(self.cache) == self.capacity:
            node = self.lru_dll.pop()
            del self.cache[node.key]
            print("evicting key: %s" % node.key)
        
        new_node = DLLNode(key, value)
        self.cache[key] = new_node
        self.lru_dll.prepend(new_node)
    
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)