from typing import Optional, Any


class Node:

    def __init__(self, value) -> None:
        self.value: Any = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


class LinkedList:

    def __init__(self, iterable=None) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._len = 0

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __len__(self): return self._len

    def __reversed__(self):
        node = self.tail
        while node is not None:
            yield node.value
            node = node.prev

    def __getitem__(self, shift):
        if not isinstance(shift, int):
            raise TypeError("Index must be type int")
        if shift >= 0:
            if shift >= self._len:
                raise IndexError("LinkedList index out of range")
            node = self.head
            for _ in range(shift):
                node = node.next
        else:
            if abs(shift) > self._len:
                raise IndexError("LinkedList index out of range")
            node = self.tail
            for _ in range(abs(shift) - 1):
                node = node.prev
        return node.value

    def __str__(self):
        return f"LinkedList({[el for el in self]})"

    def __repr__(self):
        return self.__str__()

    def append_left(self, element):
        node = Node(element)
        self._len += 1
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def pop_left(self):
        node = self.head
        if self.head is None:
            raise ValueError('cant pop from an empty linked list')
        if node is self.tail:
            self.next = self.tail = None
            self._len -= 1
            return node.value
        else:
            node.next.prev = None
            self.head = node.next
            self._len -= 1
            return node.value

    def append(self, element):
        node = Node(element)
        self._len += 1
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        node = self.tail
        if node is None:
            raise ValueError("can't pop from an empty linked list")
        if node is self.head:
            self.head = self.tail = None
            self._len -= 1
            return node.value
        else:
            self.tail = node.prev
            self.tail.next = None
            self._len -= 1
            return node.value

    def __eq__(self, __o):
        if not isinstance(__o, LinkedList):
            message = "== not supported between instances of {self.__class__.__name__!r} and {__o.__class__.__name__!r}"
            raise TypeError(message)
        else:
            if len(self) == len(__o):
                for i in range(len(self)):
                    if self[i] != __o[i]:
                        return False
                else:
                    return True
