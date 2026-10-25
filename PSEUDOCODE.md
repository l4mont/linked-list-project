# Algorithm design and pseudocode

Emory Bruington | Virginia Peninsula Community College | CSC 223
Instructor: Sally Schaffner | Created: 2026-10-24

## Representation and invariants

A Python variable holds a reference to an object. Node.data references the stored
value; Node.next references another node or None. Assigning current.data changes
what a node stores. Assigning current.next changes which node follows it.
_head identifies the first node, _tail the last, and _count the reachable length.
An empty list has both references None and count zero. A nonempty tail ends in
None. The chain has no cycles. Each operation maintains these conditions.

## Append and prepend

```text
APPEND(value)
    node = new Node(value)
    if tail is None: head = node
    else: tail.next = node
    tail = node
    count += 1

PREPEND(value)
    node = new Node(value)
    node.next = head
    head = node
    if tail is None: tail = node
    count += 1
```

Both take O(1) time and allocate one node.

## Insertion after the first matching value

```text
current = head
while current is not None and current.data != existing_value:
    current = current.next
if current is None: raise ValueError
node = new Node(new_value)
node.next = current.next
current.next = node
if tail is current: tail = node
count += 1
```

Save the old successor in node.next before redirecting current.next. Searching
costs O(n); the insertion itself costs O(1). One new node is allocated.

## Remove the first matching value

```text
previous = None; current = head
while current is not None and current.data != value:
    previous = current; current = current.next
if current is None: raise ValueError
if previous is None: head = current.next
else: previous.next = current.next
if tail is current: tail = previous
current.next = None
count -= 1
```

Removing the only node makes head and tail None. A missing value raises before
mutation. O(n) time and O(1) auxiliary space.

## Remove every match

```text
removed = 0; previous = None; current = head
while current is not None:
    next_node = current.next
    if current.data == value:
        if previous is None: head = next_node
        else: previous.next = next_node
        if tail is current: tail = previous
        current.next = None
        count -= 1; removed += 1
    else:
        previous = current
    current = next_node
return removed
```

Do not advance previous when removing current: previous must remain the last
retained node. This handles consecutive matches. O(n) time, O(1) extra space.

## Forward and backward construction

```text
BUILD_FORWARD(values)
    head = tail = None; count = 0
    for value in values from beginning to end: append(value)

BUILD_BACKWARD(values)
    head = tail = None; count = 0
    for value in values from beginning to end: prepend(value)
```

Both start from an empty state and leave the Python input list unchanged.
For calls on a populated object, this implementation replaces its contents;
the assignment's empty-object use works identically. Both take O(n) time,
allocate n nodes, and use O(1) auxiliary space beyond those nodes.

## Split existing nodes by parity

```text
if source is empty: raise ValueError
create even_list and odd_list as empty SinglyLinkedList objects
current = source.head
source.head = source.tail = None; source.count = 0
while current is not None:
    next_node = current.next
    current.next = None
    if current.data % 2 == 0: destination = even_list
    else: destination = odd_list
    if destination.tail is None: destination.head = current
    else: destination.tail.next = current
    destination.tail = current
    destination.count += 1
    current = next_node
return even_list, odd_list
```

Save next_node before setting current.next to None. Otherwise reading
current.next afterward yields None, and the unprocessed chain is lost to the
algorithm. Clearing source.head does not delete the nodes: current still refers
to the original chain. Attaching at each destination tail preserves order.

The input contract assumes simple integers. The split takes O(n) time and O(1)
auxiliary space, including the two empty list objects and a fixed number of
references. It allocates no nodes. Tests check identical node objects in the
same relative order, disjoint destinations, conserved count, correct tails,
and an emptied source. They also reject node construction and prohibited
operations during the split.

## Query and display costs

contains and full iteration take O(n) time; is_empty and len take O(1).
String conversion takes O(n) traversal time plus the cost of formatting values,
and uses memory proportional to the formatted output.
