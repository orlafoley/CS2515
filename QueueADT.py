"""
Class definitions for implementation of the Queue ADT.
Includes inefficient versions

We add to the end of the queue and pop items off the top of the queue
"""

import sys


class QueueA:
    """
    A queue using a python list, with the head at the front.

    QueueA.enqueue(x) is O(1) on average
    QueueA.dequeue() is O(n) - always has to copy the remainder of the list
    QueueA.front() is O(1)
    QueueA.length() is O(1)
    """

    def __init__(self):
        self.body = []

    def __str__(self):
        if self.length() == 0:
            return '<--|'
        out = ['']
        for item in self.body:
            out += ['<-' + str(item)]
        out += ['-|']
        return ''.join(out)

    def summary(self):
        """ Return a string summary of the queue. """
        return 'Length:' + str(self.length())

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self.body)

    def enqueue(self, item):
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        self.body += [item]

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest. """
        return self.body.pop(0)

    def length(self):
        """ Return the number of items in the queue. """
        return self.body.__len__()

    def first(self):
        """ Return the first item in the queue. """
        return self.body[0]


class QueueB:
    """
    A queue using a python list, with an internal head pointer.
    End of the list is the end of the queue.
    This queue does not wrap around.
    """

    def __init__(self):
        self.body = []
        self.head = 0

    def __str__(self):
        output = ''
        i = self.head
        while i < len(self.body):
            output += '<-' + str(self.body[i])
            i += 1
        output += '-|'
        return output

    def summary(self):
        """ Return a string summary of the queue. """
        return 'Head:' + str(self.head) + '; length:' + str(self.length())

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self.body)

    def enqueue(self, item):
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        self.body += [item]

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest. """
        item = self.body[self.head]
        self.body[self.head] = None
        self.head += 1
        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self.body.__len__() - self.head

    def first(self):
        """ Return the first item in the queue. """
        return self.body[self.head]


class Queue:
    """
    A queue using a python list, with internal wrap-around.
    Head and tail of the queue are maintained by internal pointers.
    When the list is full, a new bigger list is created.
    Unlike above, this queue does wrap around.
    """

    def __init__(self):
        self.body = [None] * 10
        self.head = 0  # index of first element, but 0 if empty
        self.tail = 0  # index of free cell for next element
        self.size = 0  # number of elements in the queue

    def __str__(self):
        output = ''
        i = self.head
        if self.head < self.tail:
            while i < self.tail:
                output += '<-' + str(self.body[i])
                i += 1
        else:
            while i < len(self.body):
                output += '<-' + str(self.body[i])
                i += 1
            i = 0
            while i < self.tail:
                output += '<-' + str(self.body[i])
                i += 1
        output += '-|'
        return output

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self.body)

    def summary(self):
        """ Return a string summary of the queue. """
        return 'Head:' + str(self.head) + '; tail:' + str(self.tail) + '; size:' + str(self.size)

    def grow(self):
        """
        Grow the internal representation of the queue.
        This should not be called externally.
        """
        oldBody = self.body
        self.body = [None] * (2 * self.size)
        oldPosition = self.head
        position = 0
        if self.head < self.tail:
            # data is not wrapped around in list
            while oldPosition <= self.tail:
                self.body[position] = oldBody[oldPosition]
                oldBody[oldPosition] = None
                position += 1
                oldPosition += 1
        else:
            # data is wrapped around
            while oldPosition < len(oldBody):
                self.body[position] = oldBody[oldPosition]
                oldBody[oldPosition] = None
                position += 1
                oldPosition += 1
            oldPosition = 0
            while oldPosition <= self.tail:
                self.body[position] = oldBody[oldPosition]
                oldBody[oldPosition] = None
                position += 1
                oldPosition += 1
        self.head, self.tail = 0, self.size

    def enqueue(self, item):
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        # An improved representation would use modular arithmetic
        if self.size == 0:
            self.body[0] = item  # assumes an empty queue has head at 0
            self.size = 1
            self.tail = 1
        else:
            self.body[self.tail] = item
            self.size += 1
            if self.size == len(self.body):  # list is now full
                self.grow()  # so grow it ready for next enqueue
            elif self.tail == len(self.body) - 1:  # no room at end, but must be at front
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest. """
        # An improved implementation would use modular arithmetic
        if self.size == 0:  # empty queue
            return None
        item = self.body[self.head]
        self.body[self.head] = None
        if self.size == 1:  # just removed last element, so rebalance
            self.head, self.tail, self.size = 0, 0, 0
        elif self.head == len(self.body) - 1:  # if head was the end of the list
            self.head = 0  # we must have wrapped round, so point to start
            self.size -= 1
        else:
            self.head += 1  # just move the pointer on one cell
            self.size -= 1
        # we haven't changed the tail, so nothing to do
        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self.size

    def first(self):
        """ Return the first item in the queue. """
        return self.body[self.head]  # will return None if queue is empty


def platinumTrophies(queue):
    # All platinum trophies are dequeued from PS3 list
    queue.enqueue(" Assassin's Creed 2 ")
    queue.enqueue(" Skyrim ")
    queue.enqueue(" Minecraft ")
    queue.enqueue(" Fallout: New Vegas ")
    queue.dequeue()
    queue.enqueue(" Assassin's Creed: Brotherhood ")
    queue.enqueue(" Assassin's Creed: Revelations ")
    queue.enqueue(" Assassin's Creed 3 ")
    queue.enqueue(" Assassin's Creed 4: Black Flag ")
    queue.dequeue()
    queue.enqueue(" Batman: Arkham City ")
    queue.enqueue(" Battlefield 2 ")
    queue.enqueue(" Call of Duty: Black Ops 2 ")
    queue.enqueue(" Call of Duty: Modern Warfare 2 ")
    queue.enqueue(" Rocksmith ")
    queue.enqueue(" Rocksmith 2014 ")
    queue.dequeue()
    queue.enqueue(" Singstar ")
    queue.enqueue(" Uncharted 1 ")
    queue.enqueue(" GTA V ")
    queue.enqueue(" GTA San Andreas ")
    queue.dequeue()
    print(queue)


# platinumTrophies(Queue())
