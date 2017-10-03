'''
Created on Oct 2, 2017

@author: vaisharm
'''
'''
he topmost node is called root of the tree. The elements that are directly under an element are called its children. The element directly above something is called its parent. 
For example, a is a child of f and f is the parent of a. Finally, elements with no children are called leaves.
tree
      ----
       j    <-- root
     /   \
    f      k  
  /   \      \
 a     h      z    <-- leaves 
 
 
 Binary Tree: A tree whose elements have at most 2 children is called a binary tree. 
 Since each element in a binary tree can have only 2 children, 
 we typically name them the left and right child.
'''

class Node:
    
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
        
#Creating the root node        
root = Node(1)
''' following is the tree after above statement
        1
      /   \
'''

root.left = Node(2)
root.right = Node(3)

''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''
   
   
root.left.left = Node(4)

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''


if __name__ == '__main__':
    pass