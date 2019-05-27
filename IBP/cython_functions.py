
from __future__ import division
import numpy as np
import math

np.random.seed(123)

def new_K(alpha,X,N,Z,s_x,s_a,obj):
    k_prob = np.zeros(5)
    for i in range(0,5):
        l = alpha/N
        new_zi = np.zeros((N,i))
        new_zi[obj,:] = np.ones((1,i))
        new_Z = np.hstack([Z,new_zi.reshape(N,i)])
        LH = full_X(new_Z,X,s_x, s_a)
        log_prior = i*np.log(l)-l-np.log(math.factorial(i))
        k_prob[i] = LH + log_prior#likelihood*prior = posterior
 
    k_prob = np.exp(k_prob-max(k_prob))
    k_prob = k_prob/sum(k_prob)
    if (abs(sum(k_prob)-1)>0.001):
        return(sum(k_prob),'wrong k sum')
    
    new_k = np.random.choice(5,1,p = k_prob)
    return (new_k)

def full_X(Z,X,s_x,s_a):
    D = X.shape[1]
    N = Z.shape[0]
    K = Z.shape[1]
    """The constant part"""
    zz = np.dot(Z.T,Z)+((s_x**2)/(s_a**2))*np.eye(K) #zz -- K*K
    determ = np.linalg.det(zz)
    log_const = 0.5*N*D*np.log(2*np.pi)+(N-K)*D*np.log(s_x)+K*D*np.log(s_a)+0.5*D*np.log(determ)
    log_const = -log_const
    """The exponential part"""
    ii =  np.eye(N)-np.dot(np.dot(Z , np.linalg.inv(zz)) , Z.T)
    tr =  np.trace(np.dot(np.dot(X.T , ii) ,X))
    expon = -tr/(2*s_x**2)
    return(log_const+expon)

