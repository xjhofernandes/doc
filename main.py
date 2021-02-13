def find_noob():
    """ Usually the return is 'Eric' 

    :returns: Eric, obvious

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/
    """
    return "Eric"

def search_name(name):
    """ Search a name in MongoDb Collection.

    :param name: String and the first of my arguments (use any name ;).

    :returns: Find or not find name (100% complicated)

    """

    list_names = ['Joseph', 'Mariah', 'Carl']
    if name in list_names:
        return "Found!"
    else:
        return "Sorry, i can't find."

def new_function():
    """ New Function to test in netlify Deploy ;)

    :returns: PENTAKILL
    """
    return "Teste :)"        

def binary_search(arr, x):
    """ 
In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

:param arr: Integer Array
:param x: Integer number

:returns: If the number really exist in array, the function will return index of the number in integer array. Else, the function will return -1.

    """    

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

arr = [ 2, 3, 10, 4, 40 ]
x = 10

result = binary_search(arr, x)

print(result)