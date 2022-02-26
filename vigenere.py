plaintext = input('Shifrelenecek metni daxil edin : ')
key = input('Achar sozu daxil edin : ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in key:
    if len(plaintext) != len(key):
        key += i
cipher = []
ciphertext = ''
for i in range(len(plaintext)):
    if plaintext[i].isupper():
        cipher.append((alphabet.find(plaintext[i].lower()) + alphabet.find(key[i])) % len(alphabet))
        ciphertext += alphabet[cipher[i]].upper()
    elif plaintext[i].islower():
        cipher.append((alphabet.find(plaintext[i]) + alphabet.find(key[i])) % len(alphabet))
        ciphertext += alphabet[cipher[i]]
    else:
        ciphertext += plaintext[i]
print(ciphertext)
