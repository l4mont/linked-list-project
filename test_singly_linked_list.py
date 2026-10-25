"""Tests for the ADT. Emory Bruington | CSC 223 | 2026-10-24."""
import unittest
from unittest.mock import patch
from singly_linked_list import SinglyLinkedList, Node


class ListAssertions:
    def assert_chain(self, linked, expected):
        nodes = []
        current = linked._head
        while current is not None:
            self.assertNotIn(id(current), [id(node) for node in nodes], 'Cycle detected')
            nodes.append(current)
            current = current.next
        self.assertEqual([node.data for node in nodes], expected)
        self.assertEqual(list(linked), expected)
        self.assertEqual(linked._count, len(expected))
        self.assertEqual(len(linked), len(expected))
        self.assertEqual(linked.is_empty(), not expected)
        self.assertIs(linked._head, nodes[0] if nodes else None)
        self.assertIs(linked._tail, nodes[-1] if nodes else None)
        if nodes:
            self.assertIsNone(linked._tail.next)
        return nodes


class TestSinglyLinkedList(ListAssertions, unittest.TestCase):
    def make(self, values=()):
        linked = SinglyLinkedList()
        linked.build_list_forward(list(values))
        return linked

    def test_node(self):
        data = []
        node = Node(data)
        self.assertIs(node.data, data)
        self.assertIsNone(node.next)

    def test_empty(self):
        self.assert_chain(SinglyLinkedList(), [])

    def test_append_empty_and_nonempty(self):
        linked = self.make()
        linked.append(10)
        self.assert_chain(linked, [10])
        linked.append(20)
        self.assert_chain(linked, [10, 20])

    def test_prepend_empty_and_nonempty(self):
        linked = self.make()
        linked.prepend(10)
        self.assert_chain(linked, [10])
        linked.prepend(20)
        self.assert_chain(linked, [20, 10])

    def test_forward_build_preserves_input(self):
        values = [10, 20, 30, 40, 50]
        linked = self.make([99])
        linked.build_list_forward(values)
        self.assert_chain(linked, [10, 20, 30, 40, 50])
        self.assertEqual(values, [10, 20, 30, 40, 50])

    def test_backward_build_preserves_input(self):
        values = [10, 20, 30, 40, 50]
        linked = self.make([99])
        linked.build_list_backward(values)
        self.assert_chain(linked, [50, 40, 30, 20, 10])
        self.assertEqual(values, [10, 20, 30, 40, 50])

    def test_empty_builders(self):
        for method in ('build_list_forward', 'build_list_backward'):
            with self.subTest(method=method):
                linked = self.make([1])
                getattr(linked, method)([])
                self.assert_chain(linked, [])

    def test_builders_reuse_public_operations(self):
        for builder, operation in [('build_list_forward', 'append'), ('build_list_backward', 'prepend')]:
            linked = self.make()
            with patch.object(linked, operation, wraps=getattr(linked, operation)) as mock:
                getattr(linked, builder)([1, 2, 3])
                self.assertEqual([call.args for call in mock.call_args_list], [(1,), (2,), (3,)])

    def test_contains_queries_iteration(self):
        linked = self.make([1, 2, 1])
        self.assertTrue(linked.contains(2))
        self.assertFalse(linked.contains(9))
        self.assertFalse(self.make().contains(1))
        self.assert_chain(linked, [1, 2, 1])
        self.assertEqual(list(iter(linked)), [1, 2, 1])

    def test_insert_interior(self):
        linked = self.make([1, 3])
        linked.insert_after(1, 2)
        self.assert_chain(linked, [1, 2, 3])

    def test_insert_tail(self):
        linked = self.make([1, 2])
        linked.insert_after(2, 3)
        self.assert_chain(linked, [1, 2, 3])

    def test_insert_first_match(self):
        linked = self.make([1, 1])
        linked.insert_after(1, 2)
        self.assert_chain(linked, [1, 2, 1])

    def test_insert_missing_unchanged(self):
        for values in ([], [1, 2]):
            linked = self.make(values)
            before = self.assert_chain(linked, values)
            with self.assertRaisesRegex(ValueError, 'Cannot insert'):
                linked.insert_after(99, 3)
            self.assertEqual(self.assert_chain(linked, values), before)

    def test_remove_head(self):
        linked = self.make([1, 2, 3])
        linked.remove(1)
        self.assert_chain(linked, [2, 3])

    def test_remove_interior(self):
        linked = self.make([1, 2, 3])
        linked.remove(2)
        self.assert_chain(linked, [1, 3])

    def test_remove_tail(self):
        linked = self.make([1, 2, 3])
        linked.remove(3)
        self.assert_chain(linked, [1, 2])

    def test_remove_only(self):
        linked = self.make([1])
        linked.remove(1)
        self.assert_chain(linked, [])
        linked.append(2)
        self.assert_chain(linked, [2])

    def test_remove_first_match(self):
        linked = self.make([1, 2, 1])
        linked.remove(1)
        self.assert_chain(linked, [2, 1])

    def test_remove_missing_unchanged(self):
        for values in ([], [1, 2]):
            linked = self.make(values)
            before = self.assert_chain(linked, values)
            with self.assertRaisesRegex(ValueError, 'Cannot remove'):
                linked.remove(99)
            self.assertEqual(self.assert_chain(linked, values), before)

    def test_remove_all_multiple_locations(self):
        linked = self.make([2, 2, 1, 2, 3, 2, 2])
        self.assertEqual(linked.remove_all(2), 5)
        self.assert_chain(linked, [1, 3])
        linked.append(4)
        self.assert_chain(linked, [1, 3, 4])

    def test_remove_all_every_node(self):
        linked = self.make([2, 2, 2])
        self.assertEqual(linked.remove_all(2), 3)
        self.assert_chain(linked, [])

    def test_remove_all_no_match(self):
        for values in ([], [1, 3]):
            linked = self.make(values)
            self.assertEqual(linked.remove_all(2), 0)
            self.assert_chain(linked, values)

    def test_string(self):
        self.assertEqual(str(self.make()), 'Head -> None')
        self.assertEqual(str(self.make([10, 20])), 'Head -> 10 -> 20 -> None')


if __name__ == '__main__':
    unittest.main()
