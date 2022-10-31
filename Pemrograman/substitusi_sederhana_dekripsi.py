# Dekripsi Substitusi Sederhana
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'DBAF NFQBG CJ CBOVQ'
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'dekripsi' #Set sebagai 'enkripsi' atau 'deskripsi'

    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi':        #Membuat pesan rahasia 
        translated = encryptMessage(myKey, myMessage)
    if myMode == 'dekripsi':        #Membuka pesan rahasia
        translated = decryptMessage(myKey, myMessage)
    print ('Menggunakan Kunci: %s'% (myKey))
    print ('Pesan Ter%s:'% (myMode))
    print(translated)

def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList

def encryptMessage(key, massage):
    return translateMessage(key, massage, 'enkripsi')

def decryptMessage(key, massage):
    return translateMessage(key, massage, 'dekripsi')

def translateMessage(key, message, mode):
    translated = ' '
    charsA = LETTERS
    charsB = key
    if mode == 'deskripsi':
        #Untuk dekripsi dapat menggunakan kode yang sama dengan enkripsi
        #Hanya perlu menukar dimana string kunci dan huruf digunakan
        charsA, charsB = charsB, charsA

    #Ulangi setiap simbol dalam pesan
    for symbol in message:
        if symbol.upper() in charsA:
            #Enkripsi/dekripsi simbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            #simbol bukan huruf; hanya perlu tambahkan
            translated += symbol
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
