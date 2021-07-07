class SLLNode:
    def __init__(self, item, nextNode):
        self.element = item     # this is the item you turn into a node to add to the SLL
        self.next = nextNode    # your node has a pointer to the next node

    def __str__(self):
        return str(self.element)

    __repr__ = __str__

class SinglyLinkedList:
    def __init__(self):
        self._first = None       # set the top of your SLL as None by default - no node if _first
        self._size = 0           # have a _size counter for your SLL

    def __str__(self):
        out = '<-'
        while self._first is not None:
            out += self._first.element + '-'
            self._first = self._first.next
        out += '|'
        return out

    __repr__ = __str__

    def add_first(self, item):
        node = SLLNode(item, self._first)           # convert to SLL node
        self._first = node                          # the node becomes the first item in the list
        self._size += 1                             # increase the list by adding an item

    def get_first(self):
        if self._size == 0:
            return None
        return self._first

    def remove_first(self):
        if self._size == 0:
            return None
        item = self._first.element      # save the first item to return it when you remove it
        self._first = self._first.next  # reassign pointer
        self._size -= 1                 # decrease the list by removing an item
        return item

    def length(self):
        return self._size        # return _size attribute

    @staticmethod
    def test():
        mylist = SinglyLinkedList()
        mylist.add_first('d')
        mylist.add_first('c')
        mylist.add_first('e')
        mylist.remove_first()
        mylist.remove_first()
        mylist.remove_first()
        print(mylist)
        mylist.add_first('x')
        mylist.add_first('y')
        mylist.add_first('z')
        print(mylist)

# SinglyLinkedList.test()
