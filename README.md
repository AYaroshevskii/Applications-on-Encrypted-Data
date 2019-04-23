
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

s = CryptoSystem() #Creating Cryptosystem

m1, m2 = 1, 0 #Messages
C1, C2 = s.Encrypt(m1,1), s.Encrypt(m2,2) #Ciphertexts

print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))
```

    Ciphertext : [03002C63721A4C299FFA24B8, 0201CDF056AA97BD274BD481] and Decrypt: 1


## Homomorphic Properties

### Randomize


```python
C1 = s.Randomize(C1,1)
print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))

C1 = s.Randomize(C1,1)
print ("Ciphertext : {} and Decrypt: {}".format(C1,s.Decrypt(C1,1)))
```

    Ciphertext : [0200EC21AB6AAD890DC3AF8A, 020338D73957C789CEB7B4D5] and Decrypt: 1
    Ciphertext : [02038754B60A1C9374449F17, 0302F363C58F1AD4D191017F] and Decrypt: 1


### Multiply


```python
C = s.Multiply(C1,C2)
print ("{} x {} = {}".format(m1,m2,s.Decrypt(C,'T')))

m1, m2 = 1, 1
C1, C2 = s.Encrypt(m1,1), s.Encrypt(m2,2)

C = s.Multiply(C1,C2)
print ("{} x {} = {}".format(m1,m2,s.Decrypt(C,'T')))
```

    1 x 0 = 0
    1 x 1 = 1


### Add


```python
m1, m2 = 1, 0
C1, C2 = s.Encrypt(m1,1), s.Encrypt(m2,1)

C = s.Add(C1,C2)
print ("{} + {} = {}".format(m1,m2,s.Decrypt(C,1)))

m1, m2 = 0, 0
C1, C2 = s.Encrypt(m1,1), s.Encrypt(m2,1)

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
    q 4986742913091041293761503
    h 1056
    r 4722294425275607285759
    exp2 72
    exp1 56
    sign1 -1
    sign0 -1
    


## Group Testing


```python
gt = GroupTesting()
print ("Decrypted matrix for testing:")
print (np.matrix(gt.Xtest))

print ("Decrypted results: {}".format(np.array(gt.ytest)))
```

    Decrypted matrix for testing:
    [[1 1 0 1 1]
     [0 0 1 0 0]
     [1 1 1 1 1]
     [1 0 0 1 1]
     [1 0 0 0 0]]
    Decrypted results: [0 1 0 0 1]



```python
C = gt.toCi(3) #get result of 2-th sample
print ("Ciphertext : {}".format(C))
```

    Ciphertext : [(0x036FDD92B480B31E2C9E1A, 0x0126D04A33E62CC1E5AFDB), (0x03273419BBE4ACCEDA635D, 0x038DAA8E781FE3A4E2C052), (0x02A0B65C95D9C0C60DDEC8, 0x047C7DE818478454DF5AC6), (0x03AADD5DC08C38CC7F1412, 0x01FF52FFDBC7F3411269C1)]



```python
print ("Result for i-th sample: {}".format(gt.s.Decrypt(C,s='T')))
```

    Result for i-th sample: 1


## Machine Learning on Encrypted Data


```python
MLenc = MachineLearningonEncrypted(n = 10, database = None)

MLenc.just_for_test() # Random Initialization

print ("Copy of decrypted database : {}".format(MLenc.copydb))

test = [random.randint(0,1) for i in range(10)]
print ("Random input for update : {}".format(test))

MLenc.updatedb(test)
print ("Updated database : {}".format(MLenc.copydb))
```

    Copy of decrypted database : [1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    Random input for update : [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]
    Updated database : [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]



```python
MLenc.test_user_input(y = None) # Random input and compute 
```

    User input : [0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    Ciphertext : [(0x02556D5B79DC6CB39BF7CF, 0x046474D3C9F3DE2EF5A7CD), (0x0309FA0C60563F6E5FD524, 0x033B5CC5A9E566F4F80AD3), (0x009C8758A1C1DDB3ECC501, 0x006A90837DE43BB5C937E5), (0x0119035E4B7D9E38730840, 0x02DFCF171FEA40E398AFD0)]
    Result of compute : 1

