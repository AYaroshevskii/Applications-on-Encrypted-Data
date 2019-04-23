
## Cryptosystem 

#### Using:
<br>
<a href="https://eprint.iacr.org/2018/1019.pdf">Crypto scheme and Applications</a>
<br>
<a href="https://crypto.stanford.edu/pbc/">Pairing-Based Cryptography library </a>
<br>
<a href="https://github.com/debatem1/pypbc">PBC Python implementation </a>

## Examples


```python
from Cryptosystem import *
from Grouptesting import *
from MLonEnc import *
```


```python
s = CryptoSystem() #Creating Cryptosystem

m1, m2 = 1, 0 #Messages
C1,C2 = s.Encrypt(m1,1), s.Encrypt(m2,2) #Ciphertexts

print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))
```

    Ciphertext : [020351DE61189B4B3C1C344D, 0201916EB6AE4316D6BA657C] and Decrypt: 1


## Homomorphic Properties

### Randomize


```python
C1 = s.Randomize(C1,1)
print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))

C1 = s.Randomize(C1,1)
print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))
```

    Ciphertext : [0301B807547D160EBF4C51BF, 02022774BCBF20ECD2D79BCE] and Decrypt: 1
    Ciphertext : [03000115AAAB7D55B4700B6C, 02011CCF921089F6CF07073E] and Decrypt: 1


### Multiply


```python
C = s.Multiply(C1,C2)
print ("{} x {} = {}".format(m1,m2,s.Decrypt(C,'T')))

m1, m2 = 1, 1
C1,C2 = s.Encrypt(m1,1), s.Encrypt(m2,2)

C = s.Multiply(C1,C2)
print ("{} x {} = {}".format(m1,m2,s.Decrypt(C,'T')))
```

    1 x 0 = 0
    1 x 1 = 1


### Add


```python
m1, m2 = 1, 0
C1,C2 = s.Encrypt(m1,1), s.Encrypt(m2,1)

C = s.Add(C1,C2)
print ("{} + {} = {}".format(m1,m2,s.Decrypt(C,1)))

m1, m2 = 0, 0
C1,C2 = s.Encrypt(m1,1), s.Encrypt(m2,1)

C = s.Add(C1,C2)
print ("{} + {} = {}".format(m1,m2,s.Decrypt(C,1)))
```

    1 + 0 = 1
    0 + 0 = 0


### Parameters


```python
s.print_params()
```

    type a
    q 4306798232377116434773103
    h 912
    r 4722366482869645213567
    exp2 72
    exp1 7
    sign1 -1
    sign0 -1
    


## Group Testing


```python
gt = GroupTesting()
print ("Decrypted matrix for testing:")
print (np.matrix(gt.Xtest))
```

    Decrypted matrix for testing:
    [[0 0 0 0 0]
     [1 1 0 0 1]
     [0 1 1 0 0]
     [0 0 1 0 0]
     [1 1 1 1 0]]



```python
print ("Decrypted results: {}".format(np.array(gt.ytest)))
```

    Decrypted results: [0 0 0 0 0]



```python
C = gt.toCi(3) #get result of 2-th sample
print ("Ciphertext : {}".format(C))
```

    Ciphertext : [(0x001CF676445B529F07B65A, 0x03C24CA4108A537B395C80), (0x037AE5D40754A9BE769E1A, 0x01E9E6A5085D2C5D67C833), (0x0269AA3E7199C55BD5E3DD, 0x032DC2331E40260F7469C3), (0x01BB65EB2FD95231F84DDC, 0x01544CAAFECB045AFD574B)]



```python
print ("Result for i-th sample: {}".format(gt.s.Decrypt(C,s='T')))
```

    Result for i-th sample: 1


## Machine Learning on Encrypted Data


```python
MLenc = MachineLearningonEncrypted(n = 10, database = None)
```


```python
MLenc.just_for_test() # Random Initialization
```


```python
print ("Copy of decrypted database : {}".format(MLenc.copydb))
```

    Copy of decrypted database : [0, 0, 1, 1, 0, 0, 0, 1, 0, 0]



```python
test = [random.randint(0,1) for i in range(10)]
print ("Random input for update : {}".format(test))

MLenc.updatedb(test)
print ("Updated database : {}".format(MLenc.copydb))
```

    Random input for update : [0, 0, 1, 0, 1, 0, 1, 1, 0, 0]
    Updated database : [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]



```python
MLenc.test_user_input(y = None) # Random input and compute 
```

    User input : [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    Ciphertext : [(0x00A1D1CD719959BE6348FB, 0x01BF934E512D6AE957DC7D), (0x028E8F65FD03403A33C2BB, 0x03294B397192291BA58F59), (0x01A09C7B8D6C4947A54637, 0x02A4FF5494A80A73E550D6), (0x02F76F046A11C5445050B4, 0x02BB5263B4DE52248793C6)]
    Result of compute : 1

