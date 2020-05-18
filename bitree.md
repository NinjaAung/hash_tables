# Time Comeplexity of Binary Trees:

## Height

- Best Case: O(k): traverses k nodes under the current nodes.

- Worst Case:  O(k): traverses k nodes under the current nodes.

## Contains

- Best Case: o(1) If the item is at the root

- Worst Case: o(log n) recursively searches through the tree by checking the child nodes

## search

- Best Case: o(1) If the item is at the root

- Worst Case: o(lg n) recursively searches through the tree by checking the child nodes

## insert

- Best Case: o(1) If the item is at the root

- Worst Case: Case:o(lg n) recursively searches through the tree by checking the child nodes

## _find_node

- Best Case: o(1) If the item is at the root

- Worst Case: o(log n) recursively searches through the tree by checking the child nodes

## _find_parent_node

- Best Case: o(1) if the node is at the root

- Worst Case:o(lg n) searches through the children nodes

## delete

- Best Case: O(log n) deleting a node with no children

- Worst Case: O(n) a node with children

## _traverse_in_order_recursive

- Best Case: Running time: o(n) depends on the number of items in the tree


## _traverse_in_order_iterative

- Best Case: Running time: o(n) depends on the number of items in the tree

- Worst Case: Memory usage: o(log n) depends on the number of items in the tree

## _traverse_pre_order_recursive

- Running time: o(n) depends on the number of items in the tree
- Memory usage: o()n

## _traverse_pre_order_iterative

- Running time: o(n) depends on the number of items in the tree

-  Memory usage: O(n)

## _traverse_post_order_recursive

- Running time: o(n) depends on the number of items in the tree
- Memory usage: o(n) 

## _traverse_post_order_iterative

- Running time: o(n) depends on the number of items in the tree

- Memory usage: o(h) the longest the stack will get is the height of the lowest node.

## _traverse_level_order_iterative

- Running time: o(n) depends on the number of items in the tree

- Memory usage: o(n) under a skewed tree otherwise O( log n)