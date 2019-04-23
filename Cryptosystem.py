from pypbc import *

#CryptoSystem

class CryptoSystem():
    
    def __init__(self, qbits = 82, rbits = 72):
        self.__qbits = qbits
        self.__rbits = rbits
        
        self.__params = Parameters(qbits = self.__qbits, rbits = self.__rbits)
        self.__pairing = Pairing(self.__params)
        
        self.__g1 = Element.random(self.__pairing, G1)**(rbits)
        self.__g2 = Element.random(self.__pairing, G2)**(qbits)
        self.__gT = self.__pairing.apply(self.__g1, self.__g2)
        
        self.pk1, self.__sk1, self.pk2, self.__sk2 = self.__keygen()
        
    
    def __keygen(self):
        
        pk1 = [Element.random(self.__pairing, Zr) , Element.random(self.__pairing, Zr)]
        sk1, pk1 = [-pk1[1], pk1[0]] , [self.__g1 ** i for i in pk1]
        
        pk2 = [Element.random(self.__pairing, Zr) , Element.random(self.__pairing, Zr)]
        sk2, pk2 = [-pk2[1], pk2[0]] , [self.__g2 ** i for i in pk2]
        
        return pk1, sk1, pk2, sk2
    
    def Encrypt(self, m, s = 1):
        
        r = Element.random(self.__pairing, Zr)
        
        if s == 1:
            C = [self.__g1 ** (m*1)  + self.pk1[0] * r,
                 self.__g1 ** (m*0)  + self.pk1[1] * r]
            
        if s == 2:
            C = [self.__g2 ** (m*1)  + self.pk2[0] * r,
                 self.__g2 ** (m*0)  + self.pk2[1] * r]
        
        if s == "T":
            r = [Element.random(self.__pairing, Zr) for i in range(4)]
            
            g2 = self.__g2
            g1 = self.__g1
            e = self.__pairing.apply
            
            C = [self.__gT**(m*1) + e(self.pk1[0] , g2**r[0]) + e(g1**r[2], self.pk2[0]),
                 self.__gT**(0) + e(self.pk1[0] , g2**r[1]) + e(g1**r[2], self.pk2[1]),
                 self.__gT**(0) + e(self.pk1[1] , g2**r[0]) + e(g1**r[3], self.pk2[0]),
                 self.__gT**(0) + e(self.pk1[1] , g2**r[1]) + e(g1**r[3], self.pk2[1])]
            
        return C
    
    def Decrypt(self, C, s = 1):
        
        if s == 1:
            
            if C[0] * self.__sk1[0] + C[1] * self.__sk1[1] == self.__g1 ** 0:
                return 0
            else:
                return 1
            
        if s == 2:
            
            if C[0] * self.__sk2[0] + C[1] * self.__sk2[1] == self.__g2 ** 0:
                return 0
            else:
                return 1
            
        if s == "T":
            ssk = [self.__sk1[0]*self.__sk2[0] , self.__sk1[0]*self.__sk2[1],
                   self.__sk1[1]*self.__sk2[0] , self.__sk1[1]*self.__sk2[1]]
            
            d_c = C[0]*ssk[0] + C[1]*ssk[1] + C[2]*ssk[2] + C[3]*ssk[3]
            
            if d_c == self.__pairing.apply(self.__g1**0,self.__g2**0):
                return 0
            else:
                return 1
            
        return None
    
    def Randomize(self,C,s=1):
        
        l,r = [Element.random(self.__pairing, Zr) for i in range(2)]
        
        if s == 1:
            return [C[0]*l + self.pk1[0]*r, C[1]*l + self.pk1[1]*r]
        
        if s == 2:
            return [C[0]*l + self.pk2[0]*r, C[1]*l + self.pk2[1]*r]
        
        if s == 'T':
            
            g2 = self.__g2
            g1 = self.__g1
            e = self.__pairing.apply
            
            r1 = [g1**Element.random(self.__pairing, Zr) for i in range(2)]
            r2 = [g2**Element.random(self.__pairing, Zr) for i in range(2)]
            
            return  [(C[0] + e(self.pk1[0] , r2[0]) + e(r1[0], self.pk2[0])) * l ,
                     (C[1] + e(self.pk1[0] , r2[1]) + e(r1[0], self.pk2[1])) * l,
                     (C[2] + e(self.pk1[1] , r2[0]) + e(r1[1], self.pk2[0])) * l,
                     (C[3] + e(self.pk1[1] , r2[1]) + e(r1[1], self.pk2[1])) * l]
                
        
        return None
            
    def Add(self,C1,C2,s=1):
        
        if s == 1 or s == 2:
            return [C1[0] + C2[0] , C1[1] + C2[1]]
        
        if s == 'T':
            return [C1[0]+C2[0],C1[1]+C2[1] , C1[2]+C2[2] , C1[3]+C2[3]]
        
        return None
            
    def Multiply(self,C1,C2):
        
        e = self.__pairing.apply
        return [e(C1[0],C2[0]),
                e(C1[0],C2[1]),
                e(C1[1],C2[0]),
                e(C1[1],C2[1])]
    
    def print_params(self):
        
        print (self.__params)
        return None