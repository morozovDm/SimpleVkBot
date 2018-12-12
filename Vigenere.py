def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    n = 0
    for i in plaintext:
        if i.isalpha(): ciphertext += shiftAlpha(i, indexAlpha(keyword[n % len(keyword)]))
        else: ciphertext += i
        n += 1
    return ciphertext

def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    n = 0
    for i in ciphertext:
        if i.isalpha(): plaintext += shiftAlpha(i, -indexAlpha(keyword[n % len(keyword)]))
        else: plaintext += i
        n += 1
    return plaintext

def indexAlpha(letter):
    let = ord(letter)
    if (let >= ord('A') and let <= ord('Z')): let -= ord('A')
    elif (let >= ord('А') and let <= ord('Я')): let -= ord('А')
    elif (let >= ord('a') and let <= ord('z')): let -= ord('a')
    elif (let >= ord('а') and let <= ord('я')): let -= ord('а')
    else: let = -1
    return let+1

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

def main():#Def main это основная функция цикла.
        #В первой строке, в переменную enc записывается значение зашифрованного сообщение.
        #Т.е. происходит вызов функции encript, в которую передается сам текст и ключ, функция его шифрует и передаёт зашифрованное сообщение обратно,
        #и оно как раз и записывается в переменную enc.
        #Далее происходит вывод шифрованного сообщения в терминал.
        #После по такому же алгоритму происходит дешифровка.
        #В функцию дешифрования передается шифрованная строка, которая находится в переменной enc,
        #и ключ, а вывод записывается в переменную dcc и выводится в терминал.
    text = input('Введите текст для шифрования: ')
    key = input('Введите ключевое слово: ')
    enc = encrypt_viginere(text, key)
    print('Текст после шифрования: ' + enc)
    dec = decrypt_viginere(enc, key)
    print('Текст после дешифрования: ' + dec)
    
if __name__ == '__main__':
    main()
