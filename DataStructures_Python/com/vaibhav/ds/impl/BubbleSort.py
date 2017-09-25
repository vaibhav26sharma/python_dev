'''
Created on Sep 26, 2017

@author: vaisharm

In this sort a pair of 2 numbers are compared from the beginning od the list.
if Num(x)> num(x+1) then they exchange the positions. Similary the comparison goes on

'''
def bubbleSort(unsorted_list):
    
    length_list = len(unsorted_list)
    moreSwaps = True
    
    while moreSwaps:
        moreSwaps = False
        for element in range(len(unsorted_list)-1):
            if unsorted_list[element] > unsorted_list[element+1]:
                moreSwaps = True
                temp = unsorted_list[element]
                unsorted_list[element] = unsorted_list[element + 1]
                unsorted_list[element + 1] = temp
                
    return unsorted_list
    
    

if __name__ == '__main__':
    
    unsorted_list = [12,5,7,18,16,11,12,4,6]
    
    sorted_list = bubbleSort(unsorted_list)
    print sorted_list
    
    
    