
from __future__ import division
import numpy as np
import numpy.linalg
import math
from IBP import new_K
from IBP import full_X 

np.random.seed(123)

def gibbs_sampler(X,init_alpha,init_sig_x,init_sig_a,mcmc):
    N = X.shape[0]
    chain_alpha = np.zeros(mcmc)
    chain_sigma_a = np.zeros(mcmc)
    chain_sigma_x = np.zeros(mcmc)
    chain_K = np.zeros(mcmc)
    chain_Z = list()
    #initial matrix Z
    Z = np.array(np.random.choice(2,N,p = [0.5,0.5])).reshape(N,1)

    chain_alpha[0] = alpha = init_alpha 
    chain_sigma_a[0] = sigma_a = init_sig_a 
    chain_sigma_x[0] = sigma_x = init_sig_x
    chain_K[0] = K = 1
    chain_Z.append(Z)
    P = np.zeros(2)
    
    Hn = 0
    for i in range(1,mcmc):
        #gibbs
        alpha = np.random.gamma(1+K,1/(1+Hn))
        print(i,K)
        Hn = 0
        for im in range(0,N): #loop over images
            Hn = Hn + 1/(im+1)
            #sample new Z_i
            for k in range(0,K):#loop over features
                zk_sum = np.sum(Z[:,k])
                if zk_sum == 0:
                     lz = -10**5
                else:
                     lz = np.log(zk_sum)-np.log(N)
                if zk_sum == N:
                     lz0 = -10**5
                else:
                     lz0 = np.log(N-zk_sum)-np.log(N)
                Z[im,k] = 1
                P[0] = full_X(Z,X,sigma_x,sigma_a)+lz
                Z[im,k] = 0
                P[1] = full_X(Z,X,sigma_x,sigma_a)+lz0

                P=np.exp(P - max(P))
                P[0] = P[0]/(P[0]+P[1])
                if np.random.uniform(0,1,1)<P[0]:
                    Z[im,k] = 1
                else:
                    Z[im,k] = 0

            #sample K---num of new features
            new_k = new_K(alpha,X,N,Z,sigma_x,sigma_a,im)[0]
            if Z.shape[1]>(K+new_k):
                Ztemp=Z
                Ztemp[im,K:(K+new_k)]=1       
            else:
                Ztemp=np.zeros((Z.shape[0],K+new_k))
                Ztemp[0:Z.shape[0],0:Z.shape[1]]=Z
                Ztemp[im,K:(K+new_k)] = 1

            Z=Ztemp
            K = K + new_k

            #sample a new sigma_x and sigma_a with MH,invgamma(2,2) prior/invgamma(1,1) proposal
            #for mh in range(0,5):
            '''propose new sigma_x'''
            current_LH = full_X(Z,X,sigma_x,sigma_a)
            #sig_x_str = sigma_x + (np.random.rand(1)[0]-0.5)
            sig_x_str = 1/np.random.gamma(3,2)#propose a new sigma_x from invgamma(3,2)
            pos_str = full_X(Z,X,sig_x_str,sigma_a)-3*np.log(sig_x_str)-1/(2*sig_x_str)
            pos = current_LH-3*np.log(sigma_x)-1/(2*sigma_x)
            if((pos_str-pos)>0):
                sigma_x = sig_x_str
            else:
                move = np.random.rand(1)
                if(np.log(move[0]) < (pos_str-pos)):
                    sigma_x = sig_x_str
                '''propose new sigma_a'''
            #sig_a_str = sigma_a + (np.random.rand(1)[0]-0.5)
            sig_a_str = 1/np.random.gamma(3,2)
            pos_str = full_X(Z,X,sigma_x,sig_a_str)-3*np.log(sig_a_str)-1/(2*sig_a_str)
            pos = current_LH-3*np.log(sigma_a)-1/(2*sigma_a)
            if((pos_str-pos) > 0):
                sigma_a = sig_a_str
            else:
                move = np.random.rand(1)
                if(np.log(move[0]) < (pos_str-pos)):
                    sigma_a = sig_a_str

        #remove features that have only 1 object
        index = np.sum(Z,0)>1
        Z = Z[:,index]
        K = Z.shape[1]

        #store chain values                
        chain_alpha[i] = alpha
        chain_sigma_a[i] = sigma_a
        chain_sigma_x[i] = sigma_x
        chain_K[i] = K
        chain_Z.append(Z)
        
    return(chain_alpha,chain_sigma_a,chain_sigma_x,chain_K,chain_Z)