
from __future__ import division
import numpy as np
import numpy.linalg
import math
from .likelihood_old import full_X_old
#sample the number of new dishes
np.random.seed(123)

def new_Kold(alpha,X,N,Z,s_x,s_a,obj):
    k_prob = np.zeros(5)
    for i in range(0,5):
        l = alpha/N
        new_zi = np.zeros((N,i))
        new_zi[obj,:] = np.ones((1,i))
        new_Z = np.hstack([Z,new_zi.reshape(N,i)])
        LH = full_X_old(new_Z,X,s_x, s_a)
        log_prior = i*np.log(l)-l-np.log(math.factorial(i))
        k_prob[i] = LH + log_prior#likelihood*prior = posterior
 
    k_prob = np.exp(k_prob-max(k_prob))
    k_prob = k_prob/sum(k_prob)
    if (abs(sum(k_prob)-1)>0.001):
        return(sum(k_prob),'wrong k sum')
    
    new_k = np.random.choice(5,1,p = k_prob)
    return (new_k)