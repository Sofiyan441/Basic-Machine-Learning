# Metode enkripsi komposit
 
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'CABE MERAH DI DAPUR'

    #substitusi
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'enkripsi'
    
    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi': 
        translated = encryptMessage(myKey, myMessage)
        output = str(translated)
    elif myMode == 'dekripsi':
        translated = decryptMessage(myKey, myMessage)
    print ('Menggunakan Kunci: %s'% (myKey))
    print ('Pesan Ter%s Tahap 1:'% (myMode))
    print(translated)

    #transposisi
    myMessage2 = str(translated)
    myKey2 = 8

    ciphertext = encryptMessage2(myKey2, myMessage2)
    print('Pesan Terenkripsi Tahap 2 ')
    #print pesan terenkripsi
    #simbol | ("pipe" character) setelah pesan enkripsi untuk spasi
    #akhir dari pesan terenkripsi
    print(ciphertext + '|')

#Metode enkripsi substitusi
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
    translated = ''
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

#Metode enkripsi Treansposisi
def encryptMessage2(key, message):
    #tiap string pada enkripsi menunjukan kolom pada grid
    ciphertext = [''] * key

    #ulangi setiap kolom  pada enkripsi
    for column in range(key):
        currentIndex = column

        # Terus mengulagi sampai indeks baru mencapai panjang pesan
        while currentIndex < len(message):
            #tempatkan karakter pada indeks baru dalam pesan
            #di akhir kolom baru dalam list enkripsi text
            ciphertext[column] += message[currentIndex]

            #pindahkan indeks baru di atas
            currentIndex += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
