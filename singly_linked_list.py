"""Linked list ADT. Emory Bruington | CSC 223 | Sally Schaffner.
Virginia Peninsula Community College | Created 2026-10-24.
"""


class Node:
    """Store a data reference and a next-node reference."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Maintain a chain using _head, _tail, and _count."""
    def __init__(self):
        self._head = self._tail = None
        self._count = 0

    def append(self, value):
        """Add at the tail in O(1) time."""
        node = Node(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._count += 1

    def prepend(self, value):
        """Add at the head in O(1) time."""
        node = Node(value)
        node.next = self._head
        self._head = node
        if self._tail is None:
            self._tail = node
        self._count += 1

    def insert_after(self, existing_value, new_value):
        """Insert after the first match; missing value raises ValueError. O(n)."""
        current = self._head
        while current is not None and current.data != existing_value:
            current = current.next
        if current is None:
            raise ValueError(f'Cannot insert: {existing_value!r} is not in the list.')
        node = Node(new_value)
        node.next = current.next
        current.next = node
        if self._tail is current:
            self._tail = node
        self._count += 1

    def remove(self, value):
        """Remove first match; missing value raises ValueError. O(n)."""
        previous = None
        current = self._head
        while current is not None and current.data != value:
            previous, current = current, current.next
        if current is None:
            raise ValueError(f'Cannot remove: {value!r} is not in the list.')
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next
        if self._tail is current:
            self._tail = previous
        current.next = None
        self._count -= 1

    def contains(self, value):
        """Search for a value in O(n) time."""
        return any(item == value for item in self)

    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def build_list_forward(self, values):
        """Replace contents using append, preserving input. O(n)."""
        self._head = self._tail = None
        self._count = 0
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        """Replace contents using prepend, preserving input. O(n)."""
        self._head = self._tail = None
        self._count = 0
        for value in values:
            self.prepend(value)

    def remove_all(self, value):
        """Remove all matches in one traversal; return removed count. O(n)."""
        removed = 0
        previous = None
        current = self._head
        while current is not None:
            next_node = current.next
            if current.data == value:
                if previous is None:
                    self._head = next_node
                else:
                    previous.next = next_node
                if self._tail is current:
                    self._tail = previous
                current.next = None
                self._count -= 1
                removed += 1
            else:
                previous = current
            current = next_node
        return removed

    def __str__(self):
        return 'Head -> ' + ' -> '.join([*(str(value) for value in self), 'None'])
