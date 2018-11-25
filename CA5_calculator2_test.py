# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:43:40 2018

@author: PC
"""

import unittest
from calculator2 import add_Func, sub_Func, mult_Func, div_Func, sqr_Func, sqr_Rt

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.seq1 = [5,6,7,8,9,10]
        self.seq2 = [3,4,5,6,7]
        self.seq3 = [20,30,40,50,60]
        self.assertEqual(45, add_Func(self.seq1))
        self.assertEqual(25, add_Func(self.seq2))
        self.assertEqual(200, add_Func(self.seq3))
    
    def test_sub(self):
        self.seq1 = [100,25,25,10,20]
        self.seq2 = [1000,100,50,50]
        self.seq3 = [800,200,200,200,200]
        self.assertEqual(20, sub_Func(self.seq1))
        self.assertEqual(800, sub_Func(self.seq2))
        self.assertEqual(0, sub_Func(self.seq3))

    def test_mult(self):
        self.seq1 = [2,3,5]
        self.seq2 = [10,10,10]
        self.seq3 = [5,4,3]
        self.assertEqual(30, mult_Func(self.seq1))
        self.assertEqual(1000, mult_Func(self.seq2))
        self.assertEqual(60, mult_Func(self.seq3))


    def test_div(self):
        self.seq1 = [100,10,5]
        self.seq2 = [20,5,2,2]
        self.seq3 = [1000,500,10]
        self.assertEqual(2, div_Func(self.seq1))
        self.assertEqual(1, div_Func(self.seq2))
        self.assertEqual(0.2, div_Func(self.seq3))
        
    def test_sqr(self):
        self.seq1 = [2,3,5]
        self.seq2 = [5,10,10]
        self.seq3 = [10,20,10,20]
        self.assertEqual([4,9,25], sqr_Func(self.seq1))
        self.assertEqual([25,100,100], sqr_Func(self.seq2))
        self.assertEqual([100,400,100,400], sqr_Func(self.seq3))
        
        
    def test_Rt(self):
        self.seq1 = [4,9,25]
        self.seq2 = [25,100,100]
        self.seq3 = [100,400,100,400]
        self.assertEqual([2,3,5], sqr_Rt(self.seq1))
        self.assertEqual([5,10,10], sqr_Rt(self.seq2))
        self.assertEqual([10,20,10,20], sqr_Rt(self.seq3))
        

    
unittest.main()    
