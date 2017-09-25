'''
Created on Sep 26, 2017

@author: vaisharm
'''
'''
The linear search is used to find an item in a list. 
The items do not have to be in order. 
To search for an item, start at the beginning of the list and
 continue searching until either the end of the list is 
 reached or the item is found.
'''

def linearSearch(item, list):
    found = False
    position = 0
    
    while position < len(list) and not found:
        
        if list[position] == item :
            found = True
        position = position + 1
    return found
        
        
        
if __name__ == "__main__":
    
    list = [10,25,5,323,5]
    item = 23
    result = linearSearch(item,list)
    if result:
        print 'Found'
    else:
        list.append(item)
        print 'Not Found, added to the list & new list is {}'.format(list)
        
