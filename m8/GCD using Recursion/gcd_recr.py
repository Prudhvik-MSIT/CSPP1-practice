'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: GCDRecr
# Write a Python function, gcd_recur(a, b), that takes in two numbers
# and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.

def gcd_recur(a_val, b_val):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if not b_val:
        return a_val
    return gcd_recur(b_val, a_val%b_val)


def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
