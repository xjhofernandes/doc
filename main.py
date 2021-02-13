def find_noob():
    """ Usually the return is 'Eric' 

    :returns: Eric, obvious
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

print(find_noob())
search_name('Teste')