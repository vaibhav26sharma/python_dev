'''
Created on Oct 2, 2017

@author: vaisharm
'''
from com.vaibhav.ds.impl.Stack import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
   
    while index < len(symbolString) and balanced:
        symbol= symbolString[index]
        if symbol in '{([':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
                
                
        index = index + 1
    
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    
    #the index of opening and closing bracket should be
    #equal as the opens and closers lists have
    #opening and closing bracket counter-parts in same
    #positions
    return opens.index(open) == closers.index(close)


    
if __name__ == "__main__":    
    
    print parChecker('((())(())')

    print parChecker('((()))')
    
    print parChecker('{{([][])}()}')
    
    print parChecker('[{()]')