# In your own words, describe what a Binary Search Tree (BST) is. In addition, describe two important properties of a BST: depth and height. How are they different?
A binary search tree is a data structure composed of Nodes where each Node has a maximum of two children 'subtrees'. 
Nodes on the left of the subtrees are less than the root node (the topmost node) and nodes on the right are greater than or equal to the root node.
The depth of a Node is the number of edges in a path from a node to the root node. 
The height of a Node is the largest number of edges from the node to the leaf node (end node) 
The height of a tree is the largest number of edges form the root node to the leaf node. 

# In your own words, describe how an algorithm to find an item in a Binary Search Tree works.
The algorithm first checks if the item is the same value as the root node, if it is the same, great - item found. 
if it is less than the root node, the next node to check is the node to the left of the root node. 
If the item is greater than the root node, the next node to check is the node on the right. 
The algorithm recursively checks until the item is found.

# In your own words, describe what a balanced BST is.
If the difference in height of the left subtree and the height of right subtree of the root node is more than 1. 
