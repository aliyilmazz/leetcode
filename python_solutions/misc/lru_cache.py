class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.node_map = dict()
        self.head = None
        self.tail = None
        self.max_capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.node_map[key]
            if self.tail == node and node.prev:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
            if self.head != node:
                node.next = self.head
                self.head.prev = node
                node.prev = None
                self.head = node
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            node = self.node_map[key]
            if self.tail == node and node.prev:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            if self.head != node:
                node.next = self.head
                self.head.prev = node
                node.prev = None
                self.head = node
            return

        if len(self.map) == self.max_capacity:
            del self.map[self.tail.val]
            del self.node_map[self.tail.val]
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None


        new_head = Node(val=key, next=self.head, prev=None)
        self.map[key] = value
        self.node_map[key] = new_head
        if self.head:
            self.head.prev = new_head
            self.head = self.head.prev
        else:  # ll is empty
            self.head = new_head
            self.tail = new_head