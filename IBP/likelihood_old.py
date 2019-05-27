
from __future__ import division
import numpy as np
import numpy.linalg
import math

#compute likelihood
np.random.seed(123)
def full_X_old(Z,X,s_x,s_a):
    D = X.shape[1]
    N = Z.shape[0]
    K = Z.shape[1]
    """The constant part"""
    zz = np.dot(Z.T,Z)+np.diag([(s_x**2)/(s_a**2)]*K) #zz -- K*K
    determ = np.linalg.det(zz)
    log_const = 0.5*N*D*np.log(2*np.pi)+(N-K)*D*np.log(s_x)+K*D*np.log(s_a)+0.5*D*np.log(determ)
    log_const = -log_const
    """The exponential part"""
    L = np.linalg.cholesky(zz)
    inv_L = np.linalg.inv(L)
    ii =  np.eye(N)-np.dot(np.dot(np.dot(Z , inv_L.T), inv_L) , Z.T)
    tr =  np.trace(np.dot(np.dot(X.T , ii) ,X))
    expon = -tr/(2*s_x**2)
    return(log_const+expon)