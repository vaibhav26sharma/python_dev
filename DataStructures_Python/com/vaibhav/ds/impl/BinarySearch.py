'''
Created on Sep 26, 2017

@author: vaisharm
'''
from __main__ import __name__

'''
The binary search is used to find an item in an ORDERED list.
To search for an item, look in the middle of the list and 
see if the number you want is in the middle,
 above the middle or below the middle. 
 If it is in the middle, you have found the item. 
 If it is higher than the middle value, 
 then adjust the bottom of the list so that you search in a smaller list 
 starting one above the middle of the list. 
 If the number is lower than the middle value, 
 then adjust the top of the list so that you search in a smaller list
  which has its highest position one less than the middle position.
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
    
    
