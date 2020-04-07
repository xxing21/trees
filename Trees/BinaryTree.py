'''
This file implements the Node and BinaryTree classes.
These two classes are the building blocks for the BST, AVLTree, and Heap data structures.
It is crucial to get these implemented correctly in order to be able to implement the other data structures.
'''

class Queue(object):
    '''
    Level order traversal -> queue
    built on in-built list
    '''
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack(object):
    '''
    Reverse level order traversal -> stack and queue
    '''
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Node():
    '''
    You do not have to implement anything within this class.
    Given a node t, you can visualize the node by running str(t) in the python interpreter.
    This is a key method to perform debugging,
    so you should get familiar with how to visualize these strings.
    '''
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret

class BinaryTree():
    '''
    This class is relatively useless by itself,
    but it is the superclass for the BST, AVLTree, and Heap classes,
    and it provides important helper functions for these classes.
    If you don't implement all of the functions in this class correctly,
    it will be impossible to implement those other classes.
    '''

    def __init__(self, root=None):
        '''
        My version of this function is slightly modified from the video notes.
        I give the root variable a default value of None,
        which allows us to create a BinaryTree that has no elements within it.
        '''
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        This function is taken from the lecture notes videos (almost) verbatim.
        The difference is that when an incorrect input is given,
        my version raises a ValueError rather than "failing silently".
        It is always good practice to make errors as loud and explicit as possible,
        as this will reduce the effort you need for debugging.
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(self.root)
        else:
            raise ValueError('Traversal type ' + str(traversal_type) + ' is not supported.')

    def preorder_print(self, start, traversal):
        '''
        Root -> Left -> Right
        1-2-4-5-3-6-7
        '''
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''
        Left -> Root -> Right
        4-2-5-1-6-3-7
        '''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''
        Left -> Right -> Root
        4-2-5-6-3-7-1
        '''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

    def levelorder_print(self, start):
        '''
        level 1 -> 2 -> ...
        use queue
        '''
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        '''
        use queue and stack
        '''
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right: #right child first
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def to_list(self, traversal_type):
        '''
        This function is similar to the print_tree function,
        but instead of printing the tree,
        it returns the contents of the tree as a list.
        A general programming principle is that a function should return its results
        rather than print them whenever possible.
        If a function returns its results,
        we can always print the returned results if we need to visualize them.
        But by returning the results we can also do more computations on the results if needed.
        Many of the test cases for more complicated tree functions rely on this to_list function,
        so it is import to implement it correctly.
        '''
        if traversal_type == 'preorder':
            return self.preorder(self.root, [])
        elif traversal_type == 'inorder':
            return self.inorder(self.root, [])
        elif traversal_type == 'postorder':
            return self.postorder(self.root, [])
        else:
            raise ValueError('traversal_type=' + str(traversal_type) + ' is not supported.')

    def preorder(self, start, traversal):
        '''
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        '''
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        '''
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def __len__(self):
        '''
        The lecture notes videos provide a recursive and an iterative version of a "size" function
        which behaves the same as the __len__ function is supposed to.
        You may copy that code here exactly.
        We are using the dunder method __len__ because that will allow us to use the len() function
        on our BinaryTree instances.
        '''
        return self.size_(self.root)

    def size(self):
        '''
        Iterative function for size of the tree
        '''
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def size_(self, node):
        '''
        Recursive function for size of the tree
        '''
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    def height(self):
        return BinaryTree._height(self.root)

    @staticmethod
    def _height(node):
        '''
        The lecture notes videos provide (almost) the exact code you need.
        In the video, the function is not implemented as a static function,
        and so the self argument is passed in as the first argument of height.
        This makes it inconvenient to use,
        and so you should implement it as a static method.
        '''
        if node is None:
            return -1
        left_height = BinaryTree._height(node.left)
        right_height = BinaryTree._height(node.right)
        return 1 + max(left_height, right_height)

'''
# Set up tree:
#         1
#        / \
#      2    3
#     /  \  /  \
#    4    5 6   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('postorder'))
print(tree.height())
print(tree.size())
print(tree.size_(tree.root))

# tree = BinaryTree(2)
# tree.root.left = Node(7)
# tree.root.right = Node(5)
# tree.root.left.left = Node(2)
# tree.root.left.right = Node(6)
# tree.root.left.right.left = Node(5)
# tree.root.left.right.right = Node(11)
# tree.root.right.right = Node(9)
# tree.root.right.right.left = Node(4)
# print(tree.print_tree('postorder'))
'''
