#!python

class BinaryTreeNode:
    """Class creating the Node object for the binary tree"""

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return True if self.left is not None or self.right is not None else False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        inspiration from ben
        O(k): Best and worst case running time: traverses k nodes under the current nodes."""
        if self.is_leaf():
            return 0
        
        LHeight = 0
        RHeight = 0

        if self.left is not None:
            LHeight = self.left.height()
        if self.right is not None:
            RHeight = self.right.height()

        return max(LHeight, RHeight) + 1


class BinarySearchTree:
    """Class that creates the references within the Node objects.
    Creates a Tree data Structure"""
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        O(n) iterates through n nodes in the tree"""
        # Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        o(1) If the item is at the root
        o(lg n) recursively searches through the tree by checking the child nodes."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        o(1) If the item is at the root
        o(lg n) recursively searches through the tree by checking the child nodes."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        o(1) If the item is at the root
        o(lg n) recursively searches through the tree by checking the child nodes."""
        # Handle the case where the tree is empty
        new_node = BinaryTreeNode(item)
        if self.is_empty():
            # Create a new root node
            self.root = new_node
            # Increase the tree size
            self.size += 1
            return
        
        node = self.root
        while True:
            if item < node.data:
                if node.left is None:
                    self.size += 1
                    node.left = new_node
                    return
                else:
                    node = node.left
            if item > node.data:
                if node.right is None:
                    self.size += 1
                    node.right = new_node
                    return
                else:
                    node = node.right
            if item == node.data:
                return "Already in Tree"

        

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        o(1) If the item is at the root
        o(lg n) recursively searches through the tree by checking the child nodes."""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                #  Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif node.data < item:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif node.data == item:
            # Return the found node
            return node
        #  Check if the given item is less than the node's data
        elif node.data > item:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif node.data < item:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        o(1) if the node is at the root
        o(lg n) searches through the children nodes"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        if node.data == item:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Use helper methods and break this algorithm down into 3 cases
        # based on how many children/descendants the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        node = self._find_node_recursive(item, self.root)
        if node is None:
            raise ValueError
        
        self.size -= 1

        if node.is_leaf():
            if node == self.root:
                self.root = None
                return
            parent = self._find_parent_node_recursive(item, self.root)
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
        else:
            if node == self.root:
                if node.left is not None and node.right is None:
                    self.root = node.left
                elif node.left is None and node.right is not None:
                    self.root = node.right
                else:
                    predecessor = self.find_predecessor(self.root.left)
                    parent = self._find_parent_node_recursive(predecessor.data, self.root)
                    if parent != self.root:
                        parent.right = predecessor.left
                    if predecessor == self.root.left:
                        self.root.left = self.root.left.left
                    predecessor.left = self.root.left
                    predecessor.right = self.root.right

                    self.root = predecessor
            else:
                parent = self._find_parent_node_recursive(item, self.root)
                if node.left is not None and node.right is None:
                    parent.left = node.left
                elif node.left is None and node.right is not None:
                    parent.right = node.right
                else:
                    predecessor = self.find_predecessor(node.left)
                    parent = self._find_parent_node_recursive(item, predecessor)
                    parent.right = predecessor.left
                    predecessor.left = node.left
                    predecessor.right = node.right
                    node = predecessor
            
    
    def find_predecessor(self, node):
        if node.right is not None:
            return self.find_predecessor(node.right)
        else:
            return node


    def get_all_descendants(self, node, children=None):
        if children is None:
            children = []

        if node.left is not None:
            children.append(node.left)
            self.get_all_descendants(node.left, children)
        if node.right is not None:
            children.append(node.right)
            self.get_all_descendants(node.right, children)

        return children


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        TODO: Memory usage: o(log n) Why and under what conditions?"""
        # Traverse in-order without using recursion (stretch challenge)


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Visit this node's data with given function
        # Traverse left subtree, if it exists
        if node is not None:
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)


    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        TODO: Memory usage: ??? Why and under what conditions?"""


        if node is not None:
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)


    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree
        Memory usage: o(h) the longest the stack will get is the height of the lowest node."""
        # Traverse post-order without using recursion (stretch challenge)
        stack = LinkedStack()
        stack.push(node)
        while len(stack) != 0:
            pass

       
    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n) depends on the number of items in the tree        
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Create queue to store nodes not yet traversed in level-order
        # uses a linked Queue for the most efficiency. 
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while len(queue) != 0:
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    # test_binary_search_tree()
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    tree = BinarySearchTree()
    for item in items:
        tree.insert(item)

    print(tree.get_all_descendants(tree.root))
    print(tree.delete(8))
    print(tree.get_all_descendants(tree.root))