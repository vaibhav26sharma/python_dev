'''
Created on Sep 27, 2017

@author: vaisharm
'''
import unittest
from com.vaibhav.ds.impl.InsertionSort import insertionSort_v2
from com.vaibhav.ds.impl.InsertionSort import testForSort


class InsertionSortTest(unittest.TestCase):


    
    def testIfSorted(self):
        self.assertEqual(testForSort([11,2,3,5,7,9]), True)
 
        

    if __name__ == "__main__":
       #import sys;sys.argv = ['', 'Test.testName']
       unittest.main()
     
       
       