'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: GCDIter
# Write a Python function, gcd_iter(a, b), that takes in two numbers
# and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcd_iter(a_val, b_val):
    '''
    a_val, b_val: positive integers
    returns: a_val positive integer, the greatest common divisor of a_val & b_val.
    '''
    # Your code here
    gcd_val = min(a_val, b_val)
    while not (a_val%gcd_val == 0 and b_val%gcd_val == 0):
        gcd_val -= 1
    return gcd_val

def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
