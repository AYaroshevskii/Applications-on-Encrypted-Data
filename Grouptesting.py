from Cryptosystem import *
import numpy as np
import random
import copy

#Group Testing on Encrypted Data

class GroupTesting():
    
    def __init__(self,n=5,X = None, y = None):
        self.n = n
        if X == None and y == None: #Random Initialization
            self.X = self.RandomInit()
            self.y = self.RandomYInit()
        
        self.s = CryptoSystem()
        
        #Create copy of decrypted X and y for testing
        self.Xtest = copy.deepcopy(self.X)
        self.ytest = copy.deepcopy(self.y)
        
        self.encrypt()
            
    def RandomInit(self):
        return [[random.randint(0,1) for i in range(self.n)] for i in range(self.n)]
    
    def RandomYInit(self):
        return [random.randint(0,1) for i in range(self.n)]
    
    def encrypt(self):
        for i in range(self.n):
            for j in range(self.n):
                self.X[i][j] = self.s.Encrypt(self.X[i][j], s=1)
            self.y[i] = self.s.Encrypt((1-self.y[i]), s=2)
            
    def toCi(self,i): #get result of i-th sample
        C = self.s.Multiply(self.X[i][0],self.y[0])
        
        for k in range(1,self.n):
            C = self.s.Add(C, self.s.Multiply(self.X[i][k],self.y[k]),s='T')
        
        return self.s.Randomize(C,s='T')