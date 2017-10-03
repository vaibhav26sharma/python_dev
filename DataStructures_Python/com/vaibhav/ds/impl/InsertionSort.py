'''
Created on Sep 27, 2017

@author: vaisharm
'''
"""
#Implementation 1

def insertionSort(unsorted_list):
  stillSwap= True
  while stillSwap:
    stillSwap= False
    for i in range(1,len(unsorted_list)):
        
        if(unsorted_list[i]< unsorted_list[i-1]):
            stillSwap = True
            
            tmp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i-1]
            unsorted_list[i-1] = tmp
            
  return unsorted_list
             
"""

#implementation 2
def insertionSort_v2(unsorted_list):
    for index in range(1,len(unsorted_list)):
        value = unsorted_list[index]
        i = index - 1 # cz we need to compare to all the elements to the left of it
        while i >= 0:
            if value < unsorted_list[i]:
                unsorted_list[i+1] = unsorted_list[i] #shift number in slot i to slot i+1 as it is greater
                unsorted_list[i] = value #shift value to the left into i as value is less than i
                i = i-1
            else:
                break
    return unsorted_list


def testForSort(list):
    sorted_list =  insertionSort_v2(list)
    for i in range(len(sorted_list)-1):
            if sorted_list[i+1]> sorted_list[i]:
                i+=1
            else:
                return False
    return True
     
        

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    
    a = insertionSort_v2(arr)
    print "Sorted array is:"
    for i in range(len(a)):
        print "%d" %a[i]

