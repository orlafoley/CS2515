from functools import total_ordering

from BST import BSTNode


@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date=None, i_runtime=None):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = str(self._title)
        return outstr

    __repr__ = __str__

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = str(self._title) + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if other.title == self.title:
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self.title == other.title)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other.title > self.title:
            return True
        return False

    def __gt__(self, other):
        """ Return True if this movie is ordered after other.

        A movie is greater than another if it's title is alphabetically after.
        """
        if other.title > self.title:
            return False
        return True

    def getTitle(self):
        return self._title

    def getDate(self):
        return self._date

    def getTime(self):
        return self._time

    def setTitle(self, title):
        self._title = title

    def setDate(self, date):
        self._date = date

    def setTime(self, time):
        self._time = time

    title = property(getTitle, setTitle)
    date = property(getDate, setDate)
    time = property(getTime, setTime)


class MovieLib:
    """ A movie library.

    Implemented using a BST. 
    """

    def __init__(self):
        """ Initialise a movie library. """
        self.bst = None

    def __str__(self):
        """ Return a string representation of the library.

        The string will be created by an in-order traversal.
        """
        # method goes here
        return self.bst.__str__()

    __repr__ = __str__

    def size(self):
        """ Return the number of movies in the library. """
        # method goes here
        return self.bst.size()

    def search(self, title):
        """ Return Movie with matching title if there, or None.

        Args:
            title: a string representing a movie title.
        """
        # method goes here
        # Note that the BST requires an object to search for, and we don't
        # necessarily know the details of the movie we are looking for except
        # its title. But Movie objects are compared only on their titles (see
        # the __eq__ method above in the Movie class).
        # Create a new Movie object with that title, and ise that to search 
        # search the BST.
        self.bst.search(title)

    def add(self, title, date, runtime):
        """ Add a new move to the library.

        Args:
            title - the title of the movie
            date - the date the movie was released
            runtime - the running time of the movie

        Returns:
            the movie file that was added, or None
        """
        # method body goes here
        # you need to create the Movie object, then add it to the BST,
        # take what is returned from that method, and then decide what to
        # return here.
        # Remember to handle the case where the bst is empty.
        newMovie = Movie(title, date, runtime)
        if self.bst is None:
            self.bst = BSTNode(newMovie)
            return newMovie.__str__()
        return self.bst.add(newMovie)

    def remove(self, title):
        """ Remove and return the a movie object with the given title, if there.

        Args:
            title - the title of the movie to be removed
        """
        # method body goes here
        return self.bst.remove(title)

    @staticmethod
    def _testadd():
        library = MovieLib()
        library.add("Memento", "11/10/2000", 113)
        print(str(library))
        print('> adding Melvin and Howard')
        library.add("Melvin and Howard", "19/09/1980", 95)
        print(str(library))
        print('> adding a second version of Melvin and Howard')
        library.add("Melvin and Howard", "21/03/2007", 112)
        print(str(library))
        print('> adding Mellow Mud')
        library.add("Mellow Mud", "21/09/2016", 92)
        print(str(library))
        print('> adding Melody')
        library.add("Melody", "21/03/2007", 113)
        print(str(library))
        return library

    @staticmethod
    def _test():
        library = MovieLib()
        library.add("B", "b", 1)
        print('Library:', library)
        print('adding', "A")
        library.add("A", "a", 1)
        print('Library:', library)
        print('removing', "A")
        library.remove("A")
        print('Library:', library)
        print('adding', "C")
        library.add("C", "c", 1)
        print('Library:', library)
        print('removing', "C")
        library.remove("C")
        print('Library:', library)
        print('adding', "F")
        library.add("F", "f", 1)
        print('Library:', library)
        print('removing', "B")
        library.remove("B")
        print('Library:', library)
        print('adding', "C")
        library.add("C", "c", 1)
        print('Library:', library)
        print('adding', "D")
        library.add("D", "d", 1)
        print('Library:', library)
        print('adding', "C")
        library.add("C", "c", 1)
        print('Library:', library)
        print('adding', "E")
        library.add("E", "e", 1)
        print('Library:', library)
        print('removing', "B")
        library.remove("B")
        print('Library:', library)
        print('removing', "D")
        library.remove("D")
        print('Library:', library)
        print('removing', "C")
        library.remove("C")
        print('Library:', library)
        print('removing', "E")
        library.remove("E")
        print('Library:', library)
        print('adding', "L")
        library.add("L", "l", 1)
        print('Library:', library)
        print('adding', "H")
        library.add("H", "h", 1)
        print('Library:', library)
        print('adding', "I")
        library.add("I", "i", 1)
        print('Library:', library)
        print('adding', "G")
        library.add("G", "g", 1)
        print('Library:', library)
        print('removing', "L")
        library.remove("L")
        print('Library:', library)
        print('removing', "H")
        library.remove("H")
        print('Library:', library)
        print('removing', "I")
        library.remove("I")
        print('Library:', library)
        print('removing', "G")
        library.remove("G")
        print('Library:', library)


def build_library(filename):
    """ Return a library of Movie files built from filename """

    # open the file
    file = open(filename, 'r', encoding="utf8")

    # create the library
    library = MovieLib()

    filecount = 0
    count = 0

    # now cycle through the  lines in the file, adding the movies to the
    # library
    for line in file:
        filecount += 1
        inputlist = line.split('\t')
        added = library.add(inputlist[0], inputlist[1], inputlist[2])
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("read a file with", filecount, "movies")
    print("Built a library with", count, "unique movie titles")
    return library


# MovieLib._testadd()
# print('++++++++++')
# MovieLib._test()

# newlibrary = build_library('smallmovies.txt')
# print(newlibrary)
