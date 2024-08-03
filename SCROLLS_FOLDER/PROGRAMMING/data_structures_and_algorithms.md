<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\data_structures_and_algorithms.md -->




[Home](/index.html)

# College Data Structures and Algorithms Notes

## Introduction to Data Structures
### Description
Data structures are ways to organize and store data in a computer so that it can be accessed and modified efficiently.

### Table

| Data Structure | Description | Example |
|---|---|---|
| Array | Collection of elements identified by index | \([1, 2, 3, 4, 5]\) |
| Linked List | Collection of nodes, each containing data and a reference to the next node | 1 -> 2 -> 3 -> 4 -> 5 |
| Stack | LIFO (Last In First Out) data structure | push, pop |
| Queue | FIFO (First In First Out) data structure | enqueue, dequeue |
| Tree | Hierarchical data structure with nodes | Binary Tree, AVL Tree |
| Graph | Collection of nodes and edges | \( G = (V, E) \) |
| Hash Table | Data structure that maps keys to values using a hash function | Dictionary in Python |

## Arrays

### Description

Arrays are a collection of elements stored at contiguous memory locations.

### Table

| Operation       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Access          | $$ O(1) $$       | Accessing an element by index           |
| Search          | $$ O(n) $$       | Searching for an element                |
| Insertion       | $$ O(n) $$       | Inserting an element                    |
| Deletion        | $$ O(n) $$       | Deleting an element                     |

## Linked Lists

### Description

A linked list is a linear data structure where each element is a separate object, known as a node, which contains a reference to the next node.

### Table

| Operation       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Access          | $$ O(n) $$       | Accessing an element by index           |
| Search          | $$ O(n) $$       | Searching for an element                |
| Insertion       | $$ O(1) $$       | Inserting an element at the beginning   |
| Deletion        | $$ O(1) $$       | Deleting an element from the beginning  |

## Stacks

### Description

A stack is a linear data structure that follows the LIFO (Last In First Out) principle.

### Table

| Operation       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Push            | $$ O(1) $$       | Adding an element to the top            |
| Pop             | $$ O(1) $$       | Removing the top element                |
| Peek            | $$ O(1) $$       | Accessing the top element               |

## Queues

### Description

A queue is a linear data structure that follows the FIFO (First In First Out) principle.

### Table

| Operation       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Enqueue         | $$ O(1) $$       | Adding an element to the end            |
| Dequeue         | $$ O(1) $$       | Removing the front element              |
| Peek            | $$ O(1) $$       | Accessing the front element             |

## Trees
### Description
A tree is a hierarchical data structure consisting of nodes, with a single node as the root from which other nodes branch out.
### Table
| Type of Tree    | Description                             | Example                     |
|-----------------|-----------------------------------------|-----------------------------|
| Binary Tree     | Each node has at most two children      |                             |
| Binary Search Tree (BST) | Binary tree with ordered nodes |                             |
| AVL Tree        | Self-balancing binary search tree       |                             |
| B-Tree          | Generalized binary search tree          |                             |
| Heap            | Complete binary tree                    | Min-Heap, Max-Heap          |

## Graphs
### Description
A graph is a collection of nodes (vertices) connected by edges.
### Table
| Type of Graph   | Description                             | Example                     |
|-----------------|-----------------------------------------|-----------------------------|
| Undirected Graph| Edges have no direction                 | $$ G = (V, E) $$            |
| Directed Graph (Digraph) | Edges have a direction           | $$ G = (V, E) $$            |
| Weighted Graph  | Edges have weights                      | $$ G = (V, E, W) $$         |
| Unweighted Graph | Edges have no weights                   | $$ G = (V, E) $$            |

## Hash Tables
### Description
A hash table is a data structure that maps keys to values using a hash function.
### Table
| Operation       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Insert          | $$ O(1) $$       | Inserting a key-value pair              |
| Delete          | $$ O(1) $$       | Deleting a key-value pair               |
| Search          | $$ O(1) $$       | Searching for a key                     |

## Sorting Algorithms
### Description
Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator.
### Table
| Algorithm       | Time Complexity (Average) | Time Complexity (Worst) | Description                             |
|-----------------|----------------------------|-------------------------|-----------------------------------------|
| Bubble Sort     | $$ O(n^2) $$               | $$ O(n^2) $$             | Simple comparison-based sorting         |
| Selection Sort  | $$ O(n^2) $$               | $$ O(n^2) $$             | In-place comparison-based sorting       |
| Insertion Sort  | $$ O(n^2) $$               | $$ O(n^2) $$             | Simple and efficient for small data     |
| Merge Sort      | $$ O(n \log n) $$          | $$ O(n \log n) $$        | Divide and conquer algorithm            |
| Quick Sort      | $$ O(n \log n) $$          | $$ O(n^2) $$             | Efficient and commonly used             |
| Heap Sort       | $$ O(n \log n) $$          | $$ O(n \log n) $$        | Based on binary heap data structure     |
| Radix Sort      | $$ O(nk) $$                | $$ O(nk) $$              | Non-comparative integer sorting         |

## Searching Algorithms
### Description
Searching algorithms are used to retrieve information stored within some data structure.
### Table
| Algorithm       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Linear Search   | $$ O(n) $$       | Sequentially checks each element        |
| Binary Search   | $$ O(\log n) $$  | Efficiently searches a sorted array     |

## Graph Algorithms
### Description
Algorithms to traverse and find paths in graphs.
### Table
| Algorithm       | Time Complexity | Description                             |
|-----------------|------------------|-----------------------------------------|
| Depth-First Search (DFS) | $$ O(V + E) $$ | Explores as far as possible along each branch |
| Breadth-First Search (BFS) | $$ O(V + E) $$ | Explores all neighbors at the present depth   |
| Dijkstra's Algorithm | $$ O(V^2) $$ or $$ O(E + V \log V) $$ with priority queue | Finds shortest paths from a source vertex to all vertices |
| Bellman-Ford Algorithm | $$ O(VE) $$ | Finds shortest paths from a source vertex to all vertices, handles negative weights |
| Floyd-Warshall Algorithm | $$ O(V^3) $$ | Finds shortest paths between all pairs of vertices |

## Complexity Analysis
### Description
The study of the efficiency of algorithms in terms of time and space.
### Table
| Complexity Class | Description                             | Example                     |
|------------------|-----------------------------------------|-----------------------------|
| Constant Time    | $$ O(1) $$                              | Accessing an array element  |
| Logarithmic Time | $$ O(\log n) $$                         | Binary Search               |
| Linear Time      | $$ O(n) $$                              | Linear Search               |
| Linearithmic Time | $$ O(n \log n) $$                      | Merge Sort                  |
| Quadratic Time   | $$ O(n^2) $$                            | Bubble Sort                 |
| Cubic Time       | $$ O(n^3) $$                            | Floyd-Warshall Algorithm    |
| Exponential Time | $$ O(2^n) $$                            | Recursive algorithms        |

## Recursion
### Description
A method of solving problems where a function calls itself as a subroutine.
### Formula
Factorial:
$$ n! = n \times (n-1)! $$
Fibonacci Sequence:
$$ F(n) = F(n-1) + F(n-2) $$

## Dynamic Programming
### Description
A method for solving complex problems by breaking them down into simpler subproblems.
### Table
| Problem          | Description                             | Example                     |
|------------------|-----------------------------------------|-----------------------------|
| Fibonacci Sequence | Solving for $$ F(n) $$ using previously computed values | $$ F(n) = F(n-1) + F(n-2) $$ |
| Longest Common Subsequence | Finding the longest subsequence common to two sequences | Dynamic Programming Table   |
| Knapsack Problem | Finding the most valuable combination of items that doesn't exceed the capacity | 0/1 Knapsack, Fractional Knapsack |


