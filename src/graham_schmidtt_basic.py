# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:22:41 2021

@author: Percy
"""
import operator

class vector:
    def __init__(self, elems):
        self.vals = elems
        self.dim = len(self.vals)
        
    def norm(self):
        squared = [x*x for x in range(self.dim)]
        self.dot_self = sum(squared)
        mag = self.dot_self**0.5
        self.norm_vals = [x/mag for x in self.vals]
    
class tensors:
    def __init__(self, vec_1, vec_2):
        self.vec_1 = vector(vec_1)
        self.vec_2 = vector(vec_2)
        
    def __inner_prod(self, vec1, vec2):
        scal_val = 0
        for i in range(len(vec1)):
            scal_val += vec1[i]*vec2[i]
        return scal_val
        
    def project(self):
        self.vec_1.norm()
        inn_prod_self = self.vec_1.dot_self
        coeff = self.__inner_prod(self.vec_1.vals, self.vec_2.vals)/inn_prod_self
        return [x*coeff for x in self.vec_1.vals]
    
def main(*vectors):
    final_vec = [vectors[0]]+[0]*(len(vectors)-1)
    projection_list = []
    # print(final_vec)
    for i in range(len(final_vec)):
        projection_list.append([])
        for j in range(i,len(vectors)):
            # print(final_vec[i])
            # print(vectors[j])
            projection_list[i].append(tensors(final_vec[i], vectors[j]).project())
        print(vectors[i])
        print(projection_list[0][i+1] )
        _ = vectors[i] - projection_list[0][i+1] 
        for k in range(1,i):
            _ = list(map(operator.sub), _,projection_list[k][i+1])
        final_vec[i+1] = _.copy()
    return final_vec
        
        
        
        
        
    
main([1,2,3,5],[4,5,6,5],[7,8,9,5])


        
        
        
        
        