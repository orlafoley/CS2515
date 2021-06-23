# Sources
# https://github.com/pgrafov/python-avl-tree
# https://en.wikipedia.org/wiki/Binary_search_tree
# https://stackoverflow.com/questions/47312815/python-binary-search-tree-size/47313099

# Comparing strings out of ease in this assignment
# See in the .__str__() searching methods, etc.
# Getters/setters/properties added just to get rid of yellow underlines in PyCharm

from functools import total_ordering


@total_ordering
class TestClass:
    """ Represents an arbitrary thing, for testing the BST. """

    def __init__(self, field1, field2=None):
        """ Initialise an object. """
        self._field1 = field1
        self._field2 = field2

    def __str__(self):
        """ Return a short string representation of this object. """
        outstr = self._field1
        return outstr

    __repr__ = __str__

    def full_str(self):
        """ Return a full string representation of this object. """
        outstr = self._field1 + ": "
        outstr = outstr + str(self._field2)
        return outstr

    def __eq__(self, other):
        """ Return True if this object has exactly same field1 as other. """
        if other.field1 == self.field1:
            return True
        return False

    def __ne__(self, other):
        """ Return False if this object has exactly same field1 as other. """
        return not (self.field1 == other.field1)

    def __lt__(self, other):
        """ Return True if this object is ordered before other.

        A thing is less than another if it's field1 is alphabetically before.
        """
        if other.field1 > self.field1:
            return True
        return False

    def getfield1(self):
        return self._field1

    def setfield1(self, field1):
        self._field1 = field1

    def getfield2(self):
        return self._field2

    def setfield2(self, field2):
        self._field2 = field2

    field1 = property(getfield1, setfield1)
    field2 = property(getfield2, setfield2)


class BSTNode:
    """ An internal node for a Binary Search Tree.  """

    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        # method body goes here
        traversal = ''
        if self._leftchild is not None:
            traversal += '(' + str(self._leftchild)
        traversal += '(' + str(self._element) + ')'
        if self._rightchild is not None:
            traversal += str(self._rightchild) + ')'
        return traversal

    __repr__ = __str__

    # GETTERS, SETTERS, PROPERTIES

    def getElement(self):
        return self._element

    def getLeftchild(self):
        return self._leftchild

    def getRightchild(self):
        return self._rightchild

    def getParent(self):
        return self._parent

    def setElement(self, element):
        self._element = element

    def setLeftchild(self, left):
        self._leftchild = left

    def setRightchild(self, right):
        self._rightchild = right

    def setParent(self, parent):
        self._parent = parent

    element = property(getElement, setElement)
    leftchild = property(getLeftchild, setLeftchild)
    rightchild = property(getRightchild, setRightchild)
    parent = property(getParent, setParent)

    # CODE GIVEN ALREADY

    def _stats(self):
        """ Return the basic stats on the tree. """
        return 'size = ' + str(self.size()) + '; height = ' + str(self.height())

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if not self._isthisapropertree():
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self.leftchild.element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self.rightchild.element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self.parent.element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self.leftchild is not None:
            self.leftchild._print_structure()
        if self._rightchild is not None:
            self.rightchild._print_structure()

    def _properBST(self):
        """ Return True if this is the root of a proper BST; False otherwise.

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly.

        Then checks that it obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """ Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree
                maxvalue is the highest value in this subtree
        """
        minvalue = self._element
        maxvalue = self._element
        if self._leftchild is not None:
            leftstate = self._leftchild._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._element:
                return False, None, None
            minvalue = leftstate[1]

        if self._rightchild is not None:
            rightstate = self._rightchild._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._element:
                return False, None, None
            maxvalue = rightstate[2]

        return True, minvalue, maxvalue

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self.leftchild is not None:
            if self.leftchild.parent != self:
                ok = False
            if not self.leftchild._isthisapropertree():
                ok = False
        if self.rightchild is not None:
            if self.rightchild.parent != self:
                ok = False
            if not self.rightchild._isthisapropertree():
                ok = False
        if self.parent is not None:
            if self.parent.leftchild != self and self.parent.rightchild != self:
                ok = False
        return ok

    # CHILDREN CODE

    def leaf(self):
        """ Return True if this node has no children. """
        # method body goes here
        if not (isinstance(self._leftchild, BSTNode) or isinstance(self._rightchild, BSTNode)):
            return True
        return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        semi = False
        if self.leftchild.element is None and self.leftchild.element is not None:
            semi = True
        elif self.leftchild.element is not None and self.leftchild.element is None:
            semi = True
        return semi

    def full(self):
        """ Return true if this node has two children. """
        # method body goes here
        if isinstance(self._leftchild, BSTNode) and isinstance(self._rightchild, BSTNode):
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """
        # method body goes here
        if self.leaf():
            return False
        return True

    # ADDING NODES

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        # method body goes here
        if obj == self._element:
            # don't add already existing data to tree
            return None
        else:
            if self._element < obj:
                if self.rightchild is None:
                    newNode = BSTNode(obj)
                    newNode.parent = self
                    self.rightchild = newNode
                    return obj
                else:
                    return self._rightchild.add(obj)
            elif obj < self._element:
                if self.leftchild is None:
                    newNode = BSTNode(obj)
                    newNode.parent = self
                    self.leftchild = newNode
                    return obj
                else:
                    return self._leftchild.add(obj)
            else:
                return None

    # SEARCHING FOR NODES

    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST
        """
        # method body goes here
        if self.element is None:
            # empty tree
            return None
        else:
            # stuff in tree
            if self.element.__str__() < searchitem.element.__str__():
                # move to larger items
                if self.rightchild is None:
                    return None  # run out of tree
                return self.rightchild.search_node(searchitem)
                # move down a generation

            elif searchitem.element.__str__() < self.element.__str__():
                # move to smaller items
                if self.leftchild is None:
                    return None  # run out of tree
                return self.leftchild.search_node(searchitem)
                # move down a generation

            else:
                # found correct item
                return searchitem

    def search(self, searchitem):
        """ Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST

        """
        # method body goes here
        return self.search_node(BSTNode(searchitem))

    # REMOVING NODES

    def remove_node(self, searchitem):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        # if this is a full node
        # find the biggest item in the left tree
        #  - there must be a left tree, since this is a full node
        #  - the node for that item can have no right children
        # move that item up into this item
        # remove that old node, which is now a semileaf
        # return the original element
        # else if this has no children
        # find who the parent was
        # set the parent's appropriate child to None
        # wipe this node
        # return this node's element
        # else if this has no right child (but must have a left child)
        # shift leftchild up into its place, and clean up
        # return the original element
        # else this has no left child (but must have a right child)
        # shift rightchild up into its place, and clean up
        # return the original element
        if self.search(searchitem) is not None:
            # if we can find it, we can delete it
            while self.element.__str__() != searchitem.__str__():
                if self.element.__str__() > searchitem.__str__():
                    current = self.leftchild
                    return current.remove_node(searchitem)
                elif self.element.__str__() < searchitem.__str__():
                    return self.rightchild.remove_node(searchitem)
                else:
                    return self
            else:
                if self.full():
                    largestLeft = self.leftchild.findmaxnode()
                    self.remove_node(largestLeft)
                    self.element = largestLeft
                elif self.leaf():
                    if self.parent is not None:
                        if self.element.__str__() > self.parent.element.__str__():
                            self.parent.rightchild = None
                        elif self.element.__str__() < self.parent.element.__str__():
                            self.parent.leftchild = None
                else:
                    # internal
                    if self.rightchild is not None:
                        if self.parent is not None:
                            if self.rightchild.leftchild is not None:
                                self.leftchild = self.rightchild.leftchild
                            self.element = self.rightchild.element
                            self.rightchild = self.rightchild.rightchild
                            if self.leftchild is not None:
                                self.leftchild.parent = self
                            if self.rightchild is not None:
                                self.rightchild.parent = self
                        else:
                            if self.rightchild.leftchild is not None:
                                self.leftchild = self.rightchild.leftchild
                            self.element = self.rightchild.element
                            self.rightchild = self.rightchild.rightchild
                    elif self.leftchild is not None:
                        if self.parent is not None:
                            if self.leftchild.rightchild is not None:
                                self.rightchild = self.leftchild.rightchild
                            self.element = self.leftchild.element
                            self.leftchild = self.leftchild.leftchild
                            self.leftchild.parent = self
                            self.rightchild.parent = self
                        else:
                            if self.leftchild.rightchild is not None:
                                self.rightchild = self.leftchild.rightchild
                            self.element = self.leftchild.element
                            self.leftchild = self.leftchild.leftchild
            return searchitem
        return None

        # method body goes here

    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        # method body goes here
        return self.remove_node(searchitem)

    # MISC CODE

    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        # method body goes here
        if self.rightchild is not None:
            return self.rightchild.findmaxnode()
        return self.element

    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        # method body goes here
        leftSide, rightSide = -1, -1
        if self.rightchild is not None:
            rightSide = self.rightchild.height()
        if self.leftchild is not None:
            leftSide = self.leftchild.height()
        return 1 + max(rightSide, leftSide)

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree,
        including this node.
        """
        # method body goes here
        size = 1  # this is our root node
        if self is not None:
            if self.rightchild is not None:
                size += self.rightchild.size()  # recursively add
            if self.leftchild is not None:
                size += self.leftchild.size()  # recursively add
        return size

    @staticmethod
    def _testadd():
        node = BSTNode(TestClass("Memento", "11/10/2000"))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "19/09/1980"))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "21/03/2007"))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(TestClass("Mellow Mud", "21/09/2016"))
        node._print_structure()
        print('> adding Melody')
        node.add(TestClass("Melody", "21/03/2007"))
        node._print_structure()
        return node

    @staticmethod
    def _test():
        node = BSTNode(TestClass("B", "b"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(TestClass("A", "a"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove(TestClass("A"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(TestClass("F", "f"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(TestClass("D", "d"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(TestClass("E", "e"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove(TestClass("D"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove(TestClass("E"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(TestClass("L", "l"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(TestClass("H", "h"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(TestClass("I", "i"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(TestClass("G", "g"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove(TestClass("L"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove(TestClass("H"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove(TestClass("I"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove(TestClass("G"))
        print('Ordered:', node)
        node._print_structure()
        print(node)


# BSTNode._testadd()
# print('++++++++++')
# BSTNode._test()
