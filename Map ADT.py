class Map:

    """
    Array based map ADT
    getitem is O(n)
    setitem is O(n)
    contains is O(n)
    delitem is O(n)
    build full map is O(n^2)
    """

    def __init__(self):
        self._map = []

    def __str__(self):
        return str(self._map)

    def getitem(self, key):
        """return the element with given key, or None if not there"""
        for k, v in self._map:
            if key == k:
                return v
        return None

    def setitem(self, key, value):
        """assign value to element with key; add new if needed"""
        for k, v in self._map:
            if key == k:
                if v != value:
                    index = self._map.index((k, v))
                    self._map.pop(index)
        self._map += [(key, value)]
        return key, value

    def contains(self, key):
        """return True if map has some an element with key """
        out = False
        for k, v in self._map:
            if key == k:
                out = True
                break
        return out

    def delitem(self, key):
        """remove element with key, or return None if not there"""
        if self.contains(key):
            for k, v in self._map:
                out = k, v
                if key == k:
                    index = self._map.index(out)
                    self._map.pop(index)
            return out
        return None

    def length(self):
        """return the number of elements in the map"""
        return self._map.__len__()

    @staticmethod
    def test():
        birthdays = Map()
        birthdays.setitem('Mary', 'June')
        birthdays.setitem('Anna', 'July')
        birthdays.setitem('Anna', 'August')
        print(birthdays.length())
        birthdays.delitem('Anne')
        print(birthdays)
        birthdays.delitem('Anna')
        print(birthdays)

# Map.test()
