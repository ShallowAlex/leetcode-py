class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

        self.dic = dict()
    
    def get(self, key: int) -> int:
        if key in self.dic:
            self.move_to_end(key)
            return self.dic[key].value
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.move_to_end(key)
            self.dic[key].value = value
        else:
            new_node = Node(key, value)
            self.dic[key] = new_node
            new_node.pre = self.tail.pre
            new_node.next = self.tail
            self.tail.pre.next = new_node
            self.tail.pre = new_node
        if len(self.dic) > self.capacity:
            self.dic.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
            

    def move_to_end(self, key: int):
        #
        old_node = self.dic[key]
        old_node.pre.next = old_node.next
        old_node.next.pre = old_node.pre

        old_node.next = self.tail
        old_node.pre = self.tail.pre
        self.tail.pre.next = old_node
        self.tail.pre = old_node

# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity


#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         else:
#             self.move_to_end(key)
#             return self[key]


#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last = False)