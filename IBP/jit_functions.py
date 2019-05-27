from numba import jit
import numpy as np

np.random.seed(123)

@jit

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