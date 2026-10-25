"""Split tests. Emory Bruington | CSC 223 | 2026-10-24."""
import unittest
from unittest.mock import patch
from singly_linked_list import Node, SinglyLinkedList
from split_evens_odds import SplitEvensOdds
from test_singly_linked_list import ListAssertions


class TestSplitEvensOdds(ListAssertions, unittest.TestCase):
    def check_split(self, values):
        source = SplitEvensOdds()
        source.build_list_forward(values)
        original = self.assert_chain(source, values)
        # Reject replacement-node construction and every prohibited operation.
        with patch.object(Node, '__init__', side_effect=AssertionError('New node during split')), \
             patch.object(SinglyLinkedList, 'append', side_effect=AssertionError('append during split')), \
             patch.object(SinglyLinkedList, 'prepend', side_effect=AssertionError('prepend during split')), \
             patch.object(SinglyLinkedList, 'remove', side_effect=AssertionError('remove during split')), \
             patch.object(SinglyLinkedList, 'remove_all', side_effect=AssertionError('remove_all during split')):
            evens, odds = source.split_even_odd()
        even_nodes = self.assert_chain(evens, [v for v in values if v % 2 == 0])
        odd_nodes = self.assert_chain(odds, [v for v in values if v % 2 != 0])
        self.assert_chain(source, [])
        for actual, expected in [(even_nodes, [n for n in original if n.data % 2 == 0]),
                                 (odd_nodes, [n for n in original if n.data % 2 != 0])]:
            self.assertEqual(len(actual), len(expected))
            for moved, old in zip(actual, expected):
                self.assertIs(moved, old)
        self.assertEqual(len(evens) + len(odds), len(original))
        self.assertEqual({id(n) for n in even_nodes + odd_nodes}, {id(n) for n in original})
        self.assertTrue({id(n) for n in even_nodes}.isdisjoint(id(n) for n in odd_nodes))
        source.append(99)
        self.assert_chain(source, [99])

    def test_mixed(self):
        self.check_split([1, 2, 3, 4, 5, 6, 7, 8])

    def test_reference_slide_example(self):
        self.check_split([10, 13, 14, 18])

    def test_all_even(self):
        self.check_split([8, 2, 4, 6])

    def test_all_odd(self):
        self.check_split([7, 1, 5, 3])

    def test_single_even(self):
        self.check_split([2])

    def test_single_odd(self):
        self.check_split([1])

    def test_zero_negatives_duplicates(self):
        self.check_split([0, -3, -2, 4, -3, 0, 4])

    def test_empty_error(self):
        source = SplitEvensOdds()
        with self.assertRaisesRegex(ValueError, 'empty list'):
            source.split_even_odd()
        self.assert_chain(source, [])

    def test_inherited_operations(self):
        source = SplitEvensOdds()
        self.assertIsInstance(source, SinglyLinkedList)
        source.append(2)
        source.prepend(1)
        source.insert_after(2, 3)
        source.remove(1)
        self.assertEqual(source.remove_all(3), 1)
        self.assertTrue(source.contains(2))
        self.assert_chain(source, [2])
        evens, odds = source.split_even_odd()
        self.assert_chain(evens, [2])
        self.assert_chain(odds, [])


if __name__ == '__main__':
    unittest.main()
