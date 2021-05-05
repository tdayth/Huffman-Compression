""" Class for a Huffman node and its attributes. """


class TreeNode:
    """ A node in a Huffman tree.

    Attributes:

    @param int letter: letter if node is a leaf
    @param TreeNode left: left child
    @param TreeNode right: right child
    @param int num: node number
    """

    def __init__(self, letter=None, left=None, right=None):
        """ Initialize a new TreeNode.

        @param TreeNode self: TreeNode
        @param int|Node letter: store letter if node is a leaf
        @param TreeNode|Node left: left child
        @param TreeNode|Node right: right child
        @rtype: NoneType
        """
        self.letter = letter
        self.left = left
        self.right = right
        self.num = None

    def __eq__(self, other):
        """ Check whether self and other are equivalent.

        @param TreeNode self: TreeNode
        @param TreeNode|Any other: TreeNode
        @rtype: bool

        >>> a = TreeNode(7)
        >>> b = TreeNode(7)
        >>> a == b
        True
        >>> b = TreeNode(9)
        >>> a == b
        False
        """
        return (type(self) == type(other) and
                self.letter == other.letter and
                self.left == other.left and
                self.right == other.right)

    def __repr__(self):
        """ String representation of a TreeNode.

        @param TreeNode self: TreeNode
        @rtype: str
        """
        return 'TreeNode({}, {}, {})'.format(self.letter, self.left, self.right)

    def is_leaf(self):
        """ Check whether TreeNode is a leaf.

        @param TreeNode self: TreeNode
        @rtype: bool

        >>> t = TreeNode(None)
        >>> t.is_leaf()
        True
        """
        return not self.left and not self.right

class ObserveNode:
    """ Observe node from compressed file.

    Attributes:

    @param int l_type: 1 if left TreeNode is a leaf, 0 otherwise
    @param int l_data: node number/letter of left TreeNode
    @param int r_type: 1 if right TreeNode is a leaf, 0 otherwise
    @param int r_data: node number/letter of right TreeNode
    """

    def __init__(self, l_type, l_data, r_type, r_data):
        """ Initialize a new ObserveNode.

        @param ObserveNode self: this ObserveNode
        @param int l_type: for initializing
        @param int l_data: for initializing
        @param int r_type: for initializing
        @param int r_data: for initializing
        @rtype: NoneType
        """
        self.l_type = l_type
        self.l_data = l_data
        self.r_type = r_type
        self.r_data = r_data

    def __repr__(self):
        """ String repre of ObserveNode.

        @param ObserveNode self: ObserveNode
        @rtype: str
        """
        return 'ObserveNode({}, {}, {}, {})'.format(
         self.l_type, self.l_data, self.r_type, self.r_data)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
