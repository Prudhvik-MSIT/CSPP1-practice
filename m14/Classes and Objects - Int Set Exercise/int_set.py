# Exercise: int set

# Consider the following code from the last lecture video:

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        self.len = 0

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)
            self.len += 1

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
            self.len -= 1
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __repr__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
# Your task is to define the following two methods for the intSet class:
#   1. Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,
#      s1.intersect(s2)
#      would return a new intSet of integers that appear in both s1 and s2. Think carefully - what should happen if s1 and s2 have no
#      elements in common?

    def intersect(self, s2):
        newList = intSet()
        for i in self.vals:
            if i in s2.vals:
                newList.insert(i)
        return newList


#   2. Add the appropriate method(s) so that len(s) returns the number of elements in s.
    def len(self):
        return self.len

# Hint: look through the Python docs to figure out what you'll need to solve this problem.


        
def main():
    setA = intSet()
    setB = intSet()
    data=input()
    data1=input()
    l1=data.split()
    l2=data1.split()
    for i in l1:
        setA.insert(int(i))
    for j in l2:
        setB.insert(int(j))
    # print(setA,setB)
    print(setA.intersect(setB))

if __name__== "__main__":
    main()