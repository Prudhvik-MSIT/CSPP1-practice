'''
Author: Prudhvik Chirunomula
Date: 08-08-2018
'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9]
# into [1, 4, 8, 9]


def apply_to_each(list_to_be_modified, function_to_be_applied):
    '''
    function that converts the given testList = [1, -4, 8, -9] into
    [1, 4, 8, 9]
    '''
    for (iter_val, _) in enumerate(list_to_be_modified):
        list_to_be_modified[iter_val] = function_to_be_applied(
            list_to_be_modified[iter_val])

def main():
    '''
    main function
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, abs)
    print(list1)

if __name__ == "__main__":
    main()
