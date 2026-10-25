# Linked List Programming Project

Author: Emory Bruington
Institution: Virginia Peninsula Community College
Course: CSC 223 - Data Structures and Analysis of Algorithms
Instructor: Sally Schaffner
Created: 2026-10-24

Implement a singly linked list ADT and a subclass that partitions existing nodes
into stable even and odd lists. The source empties and no replacement nodes
are created. The split assumes simple integer values as specified by the course.

## Run

From this directory, with Python 3 installed:

```console
python -m unittest discover -v
python main.py
```

No external dependencies are required. Implementation lives in
singly_linked_list.py and split_evens_odds.py; main.py is the user demonstration.
Separate test modules cover the ADT and splitting. PSEUDOCODE.md explains each
algorithm and its complexity. The two build methods replace existing contents
with a fresh chain and do not change their Python-list inputs.

## Verified evidence

- 32 unittest tests passed; see evidence/unittest-results.txt.
- All 15 demonstration lines matched independently specified expected output;
  see evidence/main-output.txt and evidence/main-output-verification.txt.
- Split tests check object identity, order, counts, tails, no cycles, disjoint
  result lists, source emptying, and rejection of prohibited operations.
- Study references are retained unchanged under study_materials/.

IDE: Visual Studio.
