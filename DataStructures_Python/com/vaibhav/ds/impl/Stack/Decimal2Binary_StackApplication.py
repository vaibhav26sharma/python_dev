'''
Created on Oct 3, 2017

@author: vaisharm
'''
from com.vaibhav.ds.impl.Stack.Stack import Stack

def divideBy2(decimalNumber):
    
    remainderStack = Stack()
    
    while decimalNumber > 0:
        
        rem = decimalNumber%2
        remainderStack.push(rem)
        decimalNumber = decimalNumber/2
        
    binaryString = ''
    
    while not remainderStack.isEmpty():
        binaryString = binaryString + str(remainderStack.pop())
    
    return binaryString


if __name__ == "__main__":
    
    print divideBy2(42)