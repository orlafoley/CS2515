class Set:
    """Array based set"""
    def __init__(self):
        """
        Should only have each item once
        """
        self._set = []
        self._pointer = None

    def __str__(self):
        return str(self._set)

    __repr__ = __str__

    # BUILDING THE SET

    def contains(self, item):
        """true if item is an element of the set"""
        if item in self._set:
            return True
        return False

    def add(self, item):
        """
        inserts elt;
        does nothing if already an element
        """
        if not self.contains(item):
            self._set += [item]
            return item
        return None

    def delete(self, item):
        """
        remove elt;
        does nothing if not an element
        """
        if self.contains(item):
            last = self._set[-1]  # find the last item
            index = self._set.index(item)  # find the index of the item to remove
            self._set[-1], self._set[index] = item, last  # swap your items
            self._set.pop(-1)
            return item
        return None

    def length(self):
        """return the size of the set"""
        return self._set.__len__()

    # SET STUFF FROM MATHS

    def subset(self, other):
        """true if other is a subset of the set"""
        out = True
        for item in other:
            if item not in self._set:
                out = False
                break
        return out

    def properSubset(self, other):
        """true if other is a proper subset of the set"""
        if self.subset(other):
            # has to be a subset for it to be a proper subset
            if self._set.__len__() != other.__len__():
                # if its a subset and the lengths match then they have the same elements
                # this means it is a subset but not a proper subset
                return True
        return False

    def union(self, other):
        """return a new set with all elements in set or other"""
        uniqueList = [item for item in other if item not in self._set]
        return self._set + uniqueList

    def intersection(self, other):
        """return a new set with all elements in both set and other"""
        return [item for item in self._set if item in other]

    def isdisjoint(self, other):
        """true if intersection of the set and other is empty"""
        if not self.intersection(other):
            return True
        return False

    def difference(self, other):
        """return the subtraction of other from the set"""
        return [item for item in self._set if item not in other]

    # POINTER AND ADT FUNCTIONS

    def clear(self):
        """delete all elements from the set"""
        self._set = []

    def pop(self):
        """remove and return an arbitrary element"""
        if self._pointer is not None:
            # jump to None and don't pop anything here
            if self.has_next():
                # swap to pop
                self.next()
                index = self._set.index(self._pointer)
                out = self.delete(self._set[index - 1])
                return out
            self._set.pop(-1)
        return None

    def move_to_first(self):
        """
        move cursor to the first elt, in some order;
        or None
        """
        if self._set is not []:
            self._pointer = self._set[0]
        return self._pointer

    def next(self):
        """move cursor to the next elt in some order"""
        if self.has_next():
            self._pointer = self._set.index(self._pointer + 1)
        return None

    def has_next(self):
        """true if there is another elt in the order after the cursor"""
        if self._pointer is not self._set[-1]:
            return True
        return False

    def current(self):
        """return the elt at the cursor"""
        return self._pointer

    @staticmethod
    def test():
        test = Set()
        test.add(1)
        test.add(2)
        test.add(3)
        print(test)
        test.delete(2)
        print(test)
        print(test.union([4, 5, 6]))
        print(test.intersection([3, 4, 5]))
        print(test.isdisjoint([9, 8, 7]))
        print(test.subset([1, 2]))
        print(test.properSubset([3, 1]))
        test.add(10)
        test.add(1)
        test.add(2)
        test.add(3)
        print(test)
        test.move_to_first()
        print(test.pop())
        print(test)

# Set.test()
