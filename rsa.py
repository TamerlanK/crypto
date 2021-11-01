import random
#Ededin sade olub olmadigi yoxlayan funksiya
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True
#EBOB tapan funksiya
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
#Ededlerin qarsiliqli sade olub olmadigini yoxlayan funksiya
def isCoprime(x, y):
    return gcd(x, y) == 1
#Shifreni dekript etmek ucun lazim olacaq e ededidin ters modu
def modinv(x, y):
    for i in range(1, y):
        if (x * i) % y == 1:
            return x
    return None
def rsaEnc(text,n,e):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for i in range(len(text)):
        index = alphabet.find(text[i])
        new_index = ((index % n ) ** e) % n
        encrypted.append(new_index)
    return encrypted

#Istifadechiden x ve y sade ededlerini almaq
x = int(input('x sade ededini daxil edin >> '))
y = int(input('y sade ededini daxil edin >> '))
#Her iki ededin sade olmasini yoxlamaq ucun sertler
conditions = (isPrime(x), isPrime(y))

if all(conditions): #all funksiyasi icindeki her bir shert dogru olduqda true, eks halda false qaytarir
    n = x * y
    print('n =',n)
    fi = (x-1)*(y-1)
    print('fi =', fi)
    #e ededidin sechilmesi (1 < e < fi) , e ve fi aralarinda qarsiliqli sade olmalidir
    e = 0
    while isCoprime(e, fi) == False:
        e = random.randrange(1, fi) #randrange verilmish araliqda random eded qaytaran funksiyadir
    print('e =', e)
    d = modinv(e, fi) #Dekript etmek ucun istifade olunacaq
    public_key = (e, n)
    private_key = (d, n)
    #istifadechiden metn almaq
    text = input('Metni daxil edin >> ')
    print(rsaEnc(text, n, e))

else:
    print('x ve y ededleri sade olmalidir')
    x = int(input('x sade ededini daxil edin >> '))
    y = int(input('y sade ededini daxil edin >> '))

