'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: GCDRecr
# Write a Python function, gcd_recur(a, b), that takes in two numbers
# and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.

def gcd_recursion(a_val, b_val, gcd_val):
    ''' computes GCD recursively'''
    # print(a_val, b_val, gcd_val)
    if a_val%gcd_val == 0 and b_val%gcd_val == 0:
        return gcd_val
    return gcd_recursion(a_val, b_val, gcd_val-1)

def gcd_recur(a_val, b_val):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    return gcd_recursion(a_val, b_val, min(a_val, b_val))


def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
