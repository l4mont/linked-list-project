"""Stable node partition. Emory Bruington | CSC 223 | 2026-10-24."""
from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    """Inherit the ADT and split simple integer values by relinking nodes."""
    def split_even_odd(self):
        """Move existing nodes in O(n) time and O(1) auxiliary space.

        Return (even_list, odd_list), preserving order and emptying self.
        The assignment assumes simple integer data; empty input raises ValueError.
        """
        if self.is_empty():
            raise ValueError('Cannot split an empty list.')
        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()
        current = self._head
        self._head = self._tail = None
        self._count = 0
        while current is not None:
            next_node = current.next  # Save the rest of the chain before detaching.
            current.next = None
            destination = even_list if current.data % 2 == 0 else odd_list
            if destination._tail is None:
                destination._head = current
            else:
                destination._tail.next = current
            destination._tail = current
            destination._count += 1
            current = next_node
        return even_list, odd_list
