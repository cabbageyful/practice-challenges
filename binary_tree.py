"""Binary Tree with in-order traversal

    >>> zoo = BinaryTree()
    >>> zoo.root
    None
    >>> zoo.add_node('liger')
    >>> zoo.add_node('puma')
    >>> zoo.add_node('mountain lion')
    >>> zoo.add_node('tiger')
    >>> zoo.add_node('lion')
    >>> zoo.add_node('cheetah')
    >>> zoo.add_node('cougar')

    >>> zoo.find_node('maine coon')
    None
    >>> zoo.find_node('tiger')
    <Node: tiger>
    >>> zoo.root.data
    'liger'
    >>> zoo.root.left
    <Node: cheetah>
    >>> zoo.root.right
    <Node: puma>
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node: {}>'.format(self.data)


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return '<Root: {}>'.format(self.root)


    def add_node(self, new):
        # if not issubclass(new, Node):
        #     new = Node(new)

        if self.root is None:
            self.root = Node(new)

        else:
            self._add_node(new, self.root)


    def _add_node(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._add_node(data, root.left)

        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self._add_node(data, root.right)

        elif data == root.data:
            return 'Item already exists in tree.'


    def find_node(self, info):
        if self.root != None:
            return self._find_node(info, self.root)

        # if root is None or recursive call comes up empty, returns None    
        return None


    def _find_node(self, info, current_node):
        if info == current_node.data:
            print current_node
        elif info < current_node.data and current_node.left is not None:
            self._find_node(info, current_node.left)
        elif info > current_node.data and current_node.right is not None:
            self._find_node(info, current_node.right)


    def print_bin_tree(self):
        if self.root is not None:
            return self._print_bin_tree(self.root)


    def _print_bin_tree(self, current):
        if current is not None:
            self._print_bin_tree(current.left)
            print current
            self._print_bin_tree(current.right)


#######################
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\nALL GOOD IN THE HOOD!!'
