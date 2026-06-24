from typing import List

class LinkedList:
    class Node:
        def __init__(self, val: int, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def insertHead(self, val: int) -> None:
        node = self.Node(val, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = self.Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            removed = prev.next
            prev.next = removed.next
            if removed is self.tail:
                self.tail = prev
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values: List[int] = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values
        
