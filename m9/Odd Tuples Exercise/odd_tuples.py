'''
Author: Prudhvik Chirunomula
Date: 08-08-2018
'''
#Exercise : Odd Tuples
#Write a python function odd_tuples(a_tup) that takes a some numbers
# in the tuple as input and returns a tuple in which contains odd
# index values in the input tuple

def odd_tuples(a_tup):
    '''
    a_tup: a tuple

    returns: tuple, every other element of a_tup.
    '''
    # Your Code Here
    return a_tup[::2]

def main():
    '''main function'''
    data = input()
    data = data.split()
    a_tup = ()
    for j in range(len(data)):
        a_tup += ((data[j]),)
    print(odd_tuples(a_tup))

if __name__ == "__main__":
    main()
