"""User-view demonstration. Emory Bruington | CSC 223 | 2026-10-24."""
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def main():
    values = [10, 20, 30, 40, 50]
    linked = SinglyLinkedList()
    linked.build_list_forward(values)
    print('Forward:', linked)
    backward = SinglyLinkedList()
    backward.build_list_backward(values)
    print('Backward:', backward)
    linked.insert_after(20, 25)
    print('Insert 25 after 20:', linked)
    linked.remove(10)
    print('Remove 10:', linked)
    linked.append(30)
    print('Before remove_all(30):', linked)
    print('Removed matches:', linked.remove_all(30))
    print('After remove_all(30):', linked)
    source = SplitEvensOdds()
    source.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])
    print('Source before split:', source)
    evens, odds = source.split_even_odd()
    print('Evens:', evens)
    print('Odds:', odds)
    print('Source after split:', source)
    print('Counts (source, evens, odds):', len(source), len(evens), len(odds))
    source.append(12)
    source.prepend(9)
    print('Inherited prepend and append:', source)
    print('Inherited contains(12):', source.contains(12))
    try:
        source.remove(99)
    except ValueError as error:
        print('Handled error:', error)


if __name__ == '__main__':
    main()
