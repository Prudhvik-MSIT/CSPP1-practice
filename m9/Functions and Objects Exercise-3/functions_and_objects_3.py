'''
Author: Prudhvik Chirunomula
Date: 08-08-2018
'''
# Exercise : Function and Objects Exercise-3
# Implement a function that converts the given
# testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(x_val):
    '''returns square of x_val'''
    return x_val**2

def apply_to_each(list_to_be_modified, function_to_apply):
    '''Implement a function that converts the given
    testList = [1, -4, 8, -9] into [1, 16, 64, 81]
    '''
    for iter_val, _ in enumerate(list_to_be_modified):
        list_to_be_modified[iter_val] = function_to_apply(
            list_to_be_modified[iter_val])

def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, square)
    print(list1)

if __name__ == "__main__":
    main()
