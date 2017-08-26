import sys

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
        self.depth = 0

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
            return
        node = self.root
        while True:
            if value < node.value:
                if not node.left:
                    node.insert_left(value)
                    return
                else:
                    node = node.left
            elif value == node.value:
                # duplicate value, ignore
                return
            else:
                if not node.right:
                    node.insert_right(value)
                    return
                else:
                    node = node.right


    def is_superbalanced(self):
        if not self.root:
            return True

        max_depth = 0
        min_depth = sys.maxsize
        self.root.depth = 0
        stack = [self.root] # use a stack to see how deep the leaves are
        went_left = False
        while stack:
            node = stack.pop()

            if not node.left and not node.right:
                # this is a leaf
                if node.depth < min_depth:
                    min_depth = node.depth
                if node.depth > max_depth:
                    max_depth = node.depth
                if max_depth - min_depth > 1:
                    return False

            if node.left:
                node.left.depth = node.depth + 1
                stack.append(node.left)
            if node.right:
                node.right.depth = node.depth + 1
                stack.append(node.right)

        return (max_depth - min_depth) < 2


    def is_valid(self):
        """Determine if the tree is valid"""
        stack = [(self.root, None, None)]

        while stack:
            node, less_than, greater_than = stack.pop()
            if less_than and node.value > less_than:
                return False

            if more_than and node.value < more_than:
                return False

            if node.left:
                if not less_than:
                    lthan = node.value
                else:
                    lthan = less_than
                stack.append((node.left, min(lthan, node.value), more_than))

            if node.right:
                if not more_than:
                    mthan = node.value
                else:
                    mthan = more_than
                stack.append((node.right, less_than, max(mthan, node.value)))

    def next_to_largest(self):
        """Find and return next-to-largest value in the tree.
        
        The next to largest value is found by going right as far as you can,
        then up one if a leaf, or to the left and down as far as you can go.
        
        If there is no right node, go left once, then as far right as you can.
        """
        stack = [(self.root, False)]
        went_left = False
        while stack:
            node, went_right = stack.pop()
            if went_left and not node.right:
                return node.value
            
            if went_right and not node.left:
                return node.value
            
            if went_right and node.right:
                return node.value
            
            if went_right and node.left:
                stack.append((node.left, False))
                
            if not went_right and node.right:
                stack.append((node, True))
                stack.append((node.right, False))
                continue
            
            if node.left and not went_left:
                stack.append((node.left, False))
                went_left = True
        

def test_tree(values):
    """See if a binary tree is superbalanced"""
    tree = BinaryTree()
    for value in values:
        tree.add(value)
    return tree.next_to_largest()

# run your function through some test cases here
# remember: debugging is half the battle!
print test_tree([1, 2, 3, 4, 5])
print test_tree([3, 2, 1, 4, 5])
print test_tree([5, 4, 3, 2, 1])
print test_tree([3, 2, 1, 4, 5, 3.5, 3.2, 3.9])
print test_tree([5, 3, 2, 4, 1])
print test_tree([4, 2, 1, 3, 5])
