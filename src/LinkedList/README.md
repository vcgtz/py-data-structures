# Linked List
A linked list is a type of data structure used in computer science to organize data. It consists of a sequence of nodes, where each node contains two fields: a data field to store the data and a next field which is a reference (or link) to the next node in the sequence.

Unlike arrays, data elements in a linked list are not stored at contiguous locations. Each element (we call it a node) is a separate object that contains a reference or a link to the next object in the list.

## Operations
### `insert()`
- Time Complexity: `O(n)`, where n is the number of elements in the list.
- Space Complexity: `O(1)`, as we are only adding one node to the existing list.

### `insertAfter(data)`
- Time Complexity: `O(n)`, in the worst case scenario where you insert after the last node.
- Space Complexity: `O(1)`, because we are just creating a single new node and adjusting references.

### `insertAtBeginning()`
- Time Complexity: `O(1)`, as you don't need to traverse the list, you're just adding before the head.
- Space Complexity: `O(1)`, as we are only adding one node to the existing list.

### `remove()`
- Time Complexity: `O(n)`, because in the worst case you might have to traverse the entire list.
- Space Complexity: `O(1)`, as we're not using any additional space that scales with the size of the input.

### `removeAfter(data)`
- Time Complexity: `O(n)`, in the worst case where the node is the second last node.
- Space Complexity: `O(1)`, because we are not using additional space that scales with the size of the input.

### `removeAtBeginning()`
- Time Complexity: `O(1)`, since we are directly accessing the head of the list.
- Space Complexity: `O(1)`, because we're not using any additional space that scales with the size of the input.

### `search(data)`
- Time Complexity: `O(n)`, because in the worst case you might have to traverse the entire list.
- Space Complexity: `O(1)`, as we're not using any additional space that scales with the size of the input.

### `display()`
- Time Complexity: `O(n)`, as we have to traverse the entire list to print each node.
- Space Complexity: `O(1)`, as we're not using any additional space that scales with the size of the input.
