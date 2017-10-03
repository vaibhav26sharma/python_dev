'''
Created on Oct 3, 2017

@author: vaisharm
'''
from com.vaibhav.ds.impl.Stack.Stack import Stack
def baseConverter(decNumber , base):
    
    digits = '0123456789ABCDEF'
    
    remainderStack = Stack()
    
    while decNumber > 0:
        rem = decNumber% base
        remainderStack.push(rem)
        decNumber = decNumber/base
        
        
    newString = ''
    while not remainderStack.isEmpty():
        newString = newString + digits[remainderStack.pop()]
    return newString


if __name__ == "__main__":
    
    print baseConverter(25,2)
    print baseConverter(298985, 16)