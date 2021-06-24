""" Class definition for an array-based implementation of the Stack ADT.

For invalid method calls, does not throw exceptions. Instead, returns
None if a return value is expected, and otherwise ignores the request.

"""


class Stack:
    """ An array-based stack. """
    # Note that this is meant to be private
    # _list should only be accessed from the
    # methods defined in this class.
    def __init__(self):
        self._list = []

    def __str__(self):
        """ Display a stack as a string, by listing elements in sequence.
            |- denotes the bottom of the stack
            -> denotes the top of the stack.
        So '|-x-y-z-> denotes a stack with 3 elements, and z at the top.

        Normally, a method giving this level of detail in the string would not
        be provided - users of the class are only supposed to see the size
        of the stack and the top element. It is provided here so that we can
        use it for debugging and evaluation.
        """
        out = '|-'  # have some kind of "bottom" of the stack
        for element in self._list:
            out += str(element) + '-'  # add elements one by one with a dash between
        out += '->'  # added just after the last iteration as the "top" of the stack
        return out

    def pop(self):
        """ Remove and return the top element of the stack.
        If stack is |-x-y-z-> then z is removed."""
        if self.length() == 0:
            return None
        return self._list.pop()

    def push(self, element):
        """ Place element onto the top of the stack.
        If stack is |-x-y-z-> then adds a so stack is |-x-y-z-a->."""
        self._list.append(element)

    def top(self):
        """ Return but don't remove the top element of the stack.
        If stack is |-x-y-z-> then returns x."""
        if self.length() == 0:
            return None
        return self._list[-1]

    def length(self):
        """ Return the number of elements on the stack.
        If stack is |-x-y-z-> then returns 3."""
        return self._list.__len__()

    @staticmethod
    def test():
        """ Test the basic functionality of the stack.
        Class method. """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print('stack should be |-1-2-3-->, and is %s' % stack)
        print('stack.length should be 3, and is %d' % stack.length())
        print('stack.top() should be 3, and is %d' % stack.top())
        print('stack.pop() should be 3, and is %d' % stack.pop())
        print('stack should now be |-1-2-->, and is %s' % stack)
        print('stack.length() should be 2, and is %d' % stack.length())
        stack.pop()
        stack.pop()
        print('popped two more items; length() should be 0, and is %d' % (stack.length()))
        print('stack.top() should be None, and is %s' % stack.top())
        print('stack.pop() should be None, and is %s' % stack.top())
        print('stack should be |-->, and is %s' % stack)

    @staticmethod
    def fallout():
        fallout = Stack()
        fallout.push('Fallout')
        fallout.push(1)
        fallout.push('Released in 1997')
        print(fallout)
        fallout.pop()
        fallout.pop()
        fallout.push(2)
        fallout.push('Also older than I am')
        print(fallout)
        fallout.pop()
        fallout.pop()
        fallout.push(3)
        fallout.push('Lives in Vault 101 and Washington DC')
        print(fallout)
        fallout.pop()
        fallout.pop()
        fallout.push('New Vegas')
        fallout.push('I still don\'t know how to play Caravan')
        print(fallout)
        fallout.pop()
        fallout.pop()
        fallout.push(4)
        fallout.push('Can\'t wait to buy this when I get my PS4')
        print(fallout)
        fallout.pop()
        fallout.pop()
        fallout.push(76)
        fallout.push('Probably won\'t play this because its online only and my wifi is meh')
        print(fallout)

# Stack.test()
# Stack.fallout()
