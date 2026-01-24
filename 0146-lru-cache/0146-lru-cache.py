class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
     
    # Helper functions
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node: Node) -> None:
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node
    
    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)
    
    def _lru_pop(self) -> Node:
        lru = self.tail.prev
        self._remove(lru)
        return lru
    
    # -- API --
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            lru = self._lru_pop()
            del self.cache[lru.key]

        return
            

# class Node:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}    # key: value
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.prev = self.head
    
#     # Doubly Linked list Helper functions (not affect cache)
#     def _remove(self, node: Node):
#         prev_node = node.prev
#         next_node = node.next
#         prev_node.next = next_node
#         next_node.prev = prev_node
    
#     def _add_to_front(self, node: Node):
#         first = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = first
#         first.prev = node
    
#     def _move_to_front(self, node: Node):
#         self._remove(node)
#         self._add_to_front(node)

#     def _lru_pop(self) -> Node:
#         lru = self.tail.prev
#         self._remove(lru)
#         return lru
    
#     # ---- API ----
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self._move_to_front(node)
#         return node.value
    
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#             self._move_to_front(node)
#             return

#         node = Node(key, value)
#         self.cache[key] = node
#         self._add_to_front(node)
#         if len(self.cache) > self.capacity:
#             lru = self._lru_pop()
#             del self.cache[lru.key]

#         return

# class Node:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = {}    # key: value
#         self.capacity = capacity
#         self.head = Node()  # dummy: MRU side
#         self.tail = Node()  # dummy: LRU side
#         self.head.next = self.tail
#         self.tail.prev = self.head

    # Doubly linked list helpers
    # def _remove(self, node: Node) -> None:
    #     prev_node = node.prev
    #     next_node = node.next
    #     prev_node.next = next_node
    #     next_node.prev = prev_node
    
    # def _add_to_front(self, node: Node) -> None:
    #     first = self.head.next
    #     self.head.next = node
    #     node.prev = self.head
    #     node.next = first
    #     first.prev = node
    
    # def _move_to_front(self, node: Node) -> None:
    #     self._remove(node)
    #     self._add_to_front(node)

    # def _pop_lru(self) -> Node:
    #     lru = self.tail.prev    # last real node
    #     self._remove(lru)
    #     return lru
    
    # #   ---- API ----
    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1
    #     node = self.cache[key]
    #     self._move_to_front(node)
    #     return node.value
    
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         node = self.cache[key]
    #         node.value = value
    #         self._move_to_front(node)
    #         return

    #     node = Node(key, value)
    #     self.cache[key] = node
    #     self._add_to_front(node)

    #     if len(self.cache) > self.capacity:
    #         lru = self._pop_lru()
    #         del self.cache[lru.key]

    # Doubly linked list helpers
    # def _remove(self, node: Node) -> None:
    #     prev_node = self.node.prev
    #     next_node = self.node.next
    #     prev_node.next = next_node
    #     next_node.prev = prev_node
    
    # def _add_to_front(self, node: Node) -> None:
    #     first = self.head.next
    #     self.head.next = node
    #     node.prev = self.head
    #     node.next = first
    #     first.prev = node
    
    # def _move_to_front(self, node: Node) -> None:
    #     self._remove(node)
    #     self._add_to_front(node)

    # Doubly linked list helpers
    # def _remove(self, node: Node) -> None:
    #     prev_node = node.prev
    #     next_node = node.next
    #     prev_node.next = next_node
    #     next_node.prev = prev_node
    
    # def _add_to_front(self, node: Node) -> None:
    #     first = self.head.next
    #     self.head.next = node
    #     node.prev = self.head
    #     node.next = first
    #     first.prev = node

    # def _move_to_front(self, node: Node) -> None:
    #     self._remove(node)
    #     self._add_to_front(node)
    

    # def __init__(self, capacity: int):
        # # self.cache = {}
        # # self.head = Node()
        # # self.tail = Node()
        # # self.capacity = capacity
        # # self.size = 0

        # self.head.next = self.tail
        # self.tail.prev = self.head

    # def get(self, key: int) -> int:
        # if key not in self.cache:
        #     return -1
        # node = self.cache[key]
        # self.move_to_head(node)
        # return node.value

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         node = self.cache[key]
    #         node.value = value
    #         self.move_to_head(node)
    #     else:
    #         node = Node(key, value)
    #         self.cache[key] = node
    #         self.add_to_head(node)
    #         self.size += 1
    #         if self.size > self.capacity:
    #             removed_node = self.remove_tail()
    #             del self.cache[removed_node.key]
    #             self.size -= 1
    
    # def move_to_head(self, node):
    #     self.remove_node(node)
    #     self.add_to_head(node)
    
    # def remove_node(self, node):
    #     node.prev.next = node.next
    #     node.next.prev = node.prev
    
    # def add_to_head(self, node):
    #     node.prev = self.head
    #     node.next = self.head.next
    #     self.head.next.prev = node
    #     self.head.next = node
    
    # def remove_tail(self) -> Node:
    #     node = self.tail.prev
    #     self.remove_node(node)
    #     return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)