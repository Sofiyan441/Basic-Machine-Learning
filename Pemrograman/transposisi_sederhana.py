#Metode Transposisi Sederhana

def main() :
    myMessage = 'CABE MERAH DI DAPUR'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    #print pesan terenkripsi
    #simbol | ("pipe" character) setelah pesan enkripsi untuk spasi
    #akhir dari pesan terenkripsi
    print(ciphertext + '|')

def encryptMessage(key, message):
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
