# Binary search algo
# Created by: Dylan Prole 
# Time taken: 10 minutes

def binary_search(L, value, BINARY_SEARCH_COUNTER):
    '''
    L (list): The list to search through; assumed to be sorted list
    value (int): Value to find within the list
    BINARY_SEARCH_COUNTER (int): Counter to count how many binary_search recursions are performed
    '''
    BINARY_SEARCH_COUNTER += 1
    print(f'Binary search starting...this is number {BINARY_SEARCH_COUNTER} search, using list {L}.')
    # Check to see if we have an empty list
    if len(L) == 0:
        return False
    # check first element, return True if value we are after
    if len(L) == 1:
        if L[0] == value:
            return True
        else:
            return False
    middle = len(L) // 2
    if L[middle] == value:
        return True
    elif L[middle] < value:
        return binary_search(L[middle:], value, BINARY_SEARCH_COUNTER)
    elif L[middle] > value:
        return binary_search(L[:middle], value, BINARY_SEARCH_COUNTER)
    else:
        return False
    
    
        
BINARY_SEARCH_COUNTER = 0
ordered_list = list(range(1000))
print(binary_search(ordered_list, 33, BINARY_SEARCH_COUNTER))
