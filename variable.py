import numpy as np

"""
System of n equations with n unknowns
Format : Every term should be in a list of length n+1. The first number is the coefficient of the term,
         the n others are the degrees of each unknowns.
         Every term forming an equation are gathered in a list, and then every equations in another to form the system.
        
Warning, if every number entered in the system are integer, you must enter ,dtype=float  after it 

Exemple : 3x^2y is writen as [3,2,1]

        3x^(2)*y -2y^5 + 4
        2x + 3.5x^2 y^2 + 2

        is written : np.array([[[3,2,1],[-2,0,5],[4,0,0]],
                     [[2,1,0],[3.5,2,2],[2,0,0]]])
        
        x^2 + y^2 -2
        x^2 - y^2 -1
        
        is written : np.array([[[1,2,0],[1,0,2],[-2,0,0]],
                              [[1,2,0],[-1,0,2],[-1,0,0]]], dtype=float)
        
        
        
        
        [[[1,1,1,1],[-1,3,0,0],[1,1,2,0],[-3,1,1,0],[-2,0,0,0]],
              [[1,2,0,0],[-1,0,2,0],[1,0,0,2]],
              [[1,1,0,2],[-1,0,0,1],[3,1,1,1]]]
              
        
                   
        
"""
n3=3

system3= np.array([[[1,1,1,1],[-1,3,0,0],[1,1,2,0],[-3,1,1,0],[-2,0,0,0]],
              [[1,2,0,0],[-1,0,2,0],[1,0,0,2],[-0,1,1,0],[-0,0,0,0]],
              [[1,1,0,2],[-1,0,0,1],[3,1,1,1],[-0,1,1,0],[-0,0,0,0]]], dtype=float)

vector3= [1.2,0.7, 4]

