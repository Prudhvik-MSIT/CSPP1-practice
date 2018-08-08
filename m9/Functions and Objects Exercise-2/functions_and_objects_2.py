'''
Author: Prudhvik Chirunomula
Date: 08-08-2018
'''
# Exercise : Function and Objects Exercise-2
# Implement a function that converts the given testList = [1, -4, 8, -9]
# into [2, -3, 9, -8]

def inc(x_val):
    '''
    increments x_val by 1
    '''
    return x_val+1

def apply_to_each(list_to_be_modified, function_to_apply):
    '''
    function that converts the given testList = [1, -4, 8, -9] into
    [2, -3, 9, -8]
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
    # inc = 1
    apply_to_each(list1, inc)
    print(list1)

if __name__ == "__main__":
    main()
