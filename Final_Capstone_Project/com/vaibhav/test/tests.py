'''
Created on Sep 23, 2017

@author: vaisharm
'''
import unittest

class Test(unittest.TestCase):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()