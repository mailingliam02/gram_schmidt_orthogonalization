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
        #L2 Vector Norm
        squared = [x*x for x in self.vals]
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

class main:
    def __init__(self, *vectors):
        self.vectors = vectors
        self.final_vec = [vectors[0]]+[0]*(len(vectors)-1)
        self.projection_list = []
    
    def orthogonalize(self):
        for i in range(len(self.final_vec)-1):
            self.projection_list.append([])
            for j in range(i,len(self.vectors)-1):
                # print(i)
                # print(j)
                # print(self.final_vec[i])
                self.projection_list[i].append(tensors(self.final_vec[i], self.vectors[j+1]).project())
            _ = list(map(operator.sub,self.vectors[i+1],self.projection_list[0][i]))
            for k in range(1,i+1):
                _ = list(map(operator.sub, _,self.projection_list[k][i-k]))
            self.final_vec[i+1] = _.copy()
        for i in range(len(self.final_vec)):
            _ = vector(self.final_vec[i])
            _.norm()
            self.final_vec[i] = _.norm_vals
        return self.final_vec  
      
        
        



        
        
        
        
        