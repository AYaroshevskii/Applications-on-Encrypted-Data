from Cryptosystem import *
import random
import copy

class MachineLearningonEncrypted():
    
    def __init__(self,n=10,database = None):
        self.n = n
        if database == None:
            self.database = [1 for i in range(n)]
            self.adatabase = [0 for i in range(n)]
        else:
            self.database = database
            self.adatabase = [(1-x) for x in database]
        
		#create copy of data base for testing
        self.copydb = copy.deepcopy(self.database)
        self.acopydb = copy.deepcopy(self.adatabase)
        
        self.s = CryptoSystem()
        self.encodedb()
        
    
    def encodedb(self): #encode db
        for i in range(self.n):
            self.database[i] = self.s.Encrypt(self.database[i], s=1)
            self.adatabase[i] = self.s.Encrypt(self.adatabase[i], s=2)
        
    def updatedb(self,x):
        for i,xx in enumerate(x):
            if xx == 1:
                continue
            if xx == 0:
                self.database[i] = self.s.Encrypt(0, s=1)
                self.copydb[i] = 0
                self.adatabase[i] = self.s.Encrypt(1, s=2)
                self.acopydb[i] = 1
                continue
                
    def Compute(self,Cy,Cny):
    
        C1 = self.s.Add(self.adatabase[0],Cny[0],s=2)
        C2 = self.s.Add(self.database[0],Cy[0],s=1)
        C = self.s.Multiply(C2,C1)
        
        for i in range(1,self.n):
            C1 = self.s.Add(self.adatabase[i],Cny[i],s=2)
            C2 = self.s.Add(self.database[i],Cy[i],s=1)
            C3 = self.s.Multiply(C2,C1)
            C = self.s.Add(C,C3,s='T')
        
        return self.s.Randomize(C,'T')
    
    
    def test_user_input(self,y = None):
        if y == None:
            y = [random.randint(0,1) for i in range(self.n)] #Дані користувача
        ny = [(1-y[i]) for i in range(self.n)]
        
        print ("User input : {}".format(y))
        
        Cy = []
        Cny = []
        
        for i in range(self.n):
            Cy.append(self.s.Encrypt(y[i] ,s=1))
            Cny.append(self.s.Encrypt(ny[i] ,s=2))
        
        C = self.Compute(Cy,Cny)
        
        print ("Ciphertext : {}".format(C))
        print ("Result of compute : {}".format(self.s.Decrypt(C,s='T')))
        
    def just_for_test(self): #update database with random input
        for i in range(1):
            x = [random.randint(0,1) for j in range(self.n)]
            self.updatedb(x)
