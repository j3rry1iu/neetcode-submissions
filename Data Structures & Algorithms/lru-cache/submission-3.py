class Node: 
    def __init__(self, key=0, val=0): 
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head

    def _remove(self, node): 
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _addfront(self, node): 
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        node = self.cache[key]
        self._remove(node) 
        self._addfront(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._addfront(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self._addfront(node)
        
        if len(self.cache) > self.capacity: 
            lru = self.tail.next 
            self._remove(lru)
            del self.cache[lru.key]
         
        


        
