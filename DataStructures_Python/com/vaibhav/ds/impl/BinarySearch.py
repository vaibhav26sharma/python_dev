'''
Created on Sep 26, 2017

@author: vaisharm
'''
from __main__ import __name__

'''
The binary search is used to find an item in an ORDERED list.
'''

def binarySearch(item, sorted_List):
    list_length = len(sorted_List)
    found = False
    
    
    if item == sorted_List[list_length/2]:
        found= True
        return found, 'it is the center element'
    
    elif item < sorted_List[list_length/2]:
        pos = 0
        while pos < list_length/2 and not found:
            if sorted_List[pos] == item:
                found = True
            pos = pos +1    
            
            if found:
              return found,'below middle one'
        
    elif item > sorted_List[list_length/2]:
        pos = list_length - 1
        while pos > list_length/2 and not found:
            if sorted_List[pos] == item:
                found = True
            pos = pos -1   
            
            if found: 
               return found, 'above middle one'
        
        
        
           
    
if __name__ == '__main__':
    item =2
    sorted_list = [2,5,7,12,14,21,28,31,36]
    result = binarySearch(item, sorted_list)
    print result
    
    
