#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA 
import math

  
#Two aray vectors are given  
A = np.array(([2,3])) 
B = np.array(([-1,0]))
C=  np.array(([2,-4]))

#Formula for calculating the equidistance on x-axis  

#x=(np.linalg.norm((A-B)*(A-D)))
#x=(1/2)*np.linalg.norm((np.cross(A-B,A-D)))
#y=(1/2)*np.linalg.norm((np.cross(B-C,B-D)))

#print ("Area of quadrilateral ABCD is", x+y)


def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

#
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
