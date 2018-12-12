def encrypt_cesar(plaintext, key):
    ciphertext = ""
    for i in plaintext:
        if i.isalpha(): ciphertext += shiftAlpha(i, 3)
        else: ciphertext += i
    return ciphertext

def decrypt_cesar(ciphertext, key):
    plaintext = ""
    for i in ciphertext:
        if i.isalpha(): plaintext += shiftAlpha(i, -3)
        else: plaintext += i
    return plaintext

def shiftAlpha(letter, count):
    let = ord(letter)
    if (let >= ord('A') and let <= ord('Z')): let = shiftCycle(ord('A'), ord('Z'), let, count)
    elif (let >= ord('А') and let <= ord('Я')): let = shiftCycle(ord('А'), ord('Я'), let, count)
    elif (let >= ord('a') and let <= ord('z')): let = shiftCycle(ord('a'), ord('z'), let, count)
    elif (let >= ord('а') and let <= ord('я')): let = shiftCycle(ord('а'), ord('я'), let, count)      
    letter = chr(let)
    return letter

def shiftCycle(a, b, N, count):
    N += count
    if N > b: N -= b-a+1
    elif N < a: N += b-a+1
    return N

def main():
    enc =encrypt_cesar('ABCabcXYZxyzАБВабвЭЮЯэюя',3)
    print(enc)
    dcc = decrypt_cesar(enc,-3)
    print(dcc)

if __name__ == '__main__':
    main()
