# -*- coding: utf-8 -*-
import unittest 
from src.graham_schmidtt_basic import vector, tensors, main
class TestDataset(unittest.TestCase):        
    def test_vector_norm_mag(self):
        test_case = [1,2,3]
        vector_inst = vector(test_case)
        vector_inst.norm()
        predicted = vector_inst.dot_self**0.5
        actual = 3.7416573867739413
        self.assertEqual(actual,predicted)
    
    def test_vector_norm_vector(self):
        test_case = [1,2,3]
        vector_inst = vector(test_case)
        vector_inst.norm()
        predicted = vector_inst.norm_vals
        actual = [1/3.7416573867739413, 2/3.7416573867739413, 3/3.7416573867739413]
        self.assertEqual(actual,predicted)
        
    def test_tensors_inner_prod(self):
        test_case = [[1,2,3], [3,4,5]]
        tensor_inst = tensors(test_case[0], test_case[1])
        predicted = tensor_inst._tensors__inner_prod(tensor_inst.vec_1.vals, tensor_inst.vec_2.vals)
        actual = 26
        self.assertEqual(actual, predicted)
        
    def test_tensors_project(self):
        test_case = [[1,0,3], [-1,4,2]]
        tensor_inst = tensors(test_case[0], test_case[1])
        predicted = tensor_inst.project()
        actual = [0.5, 0, 1.5]
        self.assertEqual(actual, predicted)       
    
    def test_main_3_vec3D(self):
        test_case = [[1,2,3], [0,-1,6], [-5,5,0]]
        main_inst = main(test_case[0],test_case[1],test_case[2])
        predicted = main_inst.orthogonalize()
        actual = [[0.2672612419124244, 0.5345224838248488, 0.8017837257372732],[-0.26418327467353053, -0.7595269146864003, 0.5944123680154438],[-0.9267030948228231, 0.3706812379291293, 0.06178020632152154]]
        self.assertEqual(actual,predicted)
        
    def test_main_4_vec4D(self):
        test_case = [[1,2,3,4], [0,-1,6,3],[-5,5,0,-9],[15,0,3,-9]]
        main_inst = main(test_case[0],test_case[1],test_case[2],test_case[3])
        predicted = main_inst.orthogonalize()
        actual = [[0.1826,0.3652,0.5477,0.7303],[-0.2094,-0.6432,0.7179,-0.1645],[-0.4142,0.6675,0.3621,-0.5018],[0.8668,0.0867,0.2311,-0.4334]]
        actual = [[0.18257418583505536, 0.3651483716701107, 0.5477225575051661, 0.7302967433402214],[-0.20939884125839364,-0.6431535838650662, 0.7179388843144925, -0.16452766098873786], [-0.41420611431382376, 0.6674635670657045,0.3621344885143717,-0.501781121340175], [0.8667479949854814,0.08667479949854817,0.23113279866279504,-0.4333739974927407]]
        self.assertEqual(actual,predicted)
        
