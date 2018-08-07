'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: Is In
# Write a Python function, is_in(char, a_str), that takes in two arguments
# a character and String and returns the is_in(char, a_str) which retuns a
# boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def is_in(char, a_str):
    '''
    char: a single character
    a_str: an alphabetized string

    returns: True if char is in a_str; False otherwise
    '''
    # Your code here
    len_str = len(a_str)
    # print(a_str,len_str)
    if len_str == 0:
        return False
    if a_str[len_str//2] == char:
        return True
    elif a_str[len_str//2] > char:
        return is_in(char, a_str[0:len_str//2])
    return is_in(char, a_str[len_str//2:])

def main():
    '''main function'''
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
