alphabhet = 'abcdefghijklmnopqrstuvwxyz'

# function encryption based on rot 13


def encrypt(text):
    # mengubah text menjadi bentuk lowercase
    text = text.lower()

    # penyimpanan variable pada hasil enripsi
    hasil = ''

    # Iterasi setiap karakter dalam teks
    for char in text:
        # Periksa apakah karakter merupakan huruf abjad
        if char.isalpha():
            # Enkripsi karakter dengan menggeser 13 posisi ke depan
            hasil += alphabhet[(alphabhet.index(char) + 13) % 26]
        else:
            # Jika karakter bukan huruf abjad, biarkan tidak berubah
            hasil += char
    return hasil


# Fungsi untuk dekripsi berdasarkan rot 13 dengan menggeser 13 posisi ke belakang
def decrypt(text):
    # Ubah teks input ke huruf kecil
    text = text.lower()

    # penyimpanan variable
    hasil = ''

    # pengaturan posisi

    for char in text:
        # Periksa apakah karakter merupakan huruf abjad
        if char.isalpha():
            # Dekripsi karakter dengan menggeser 13 posisi ke belakang
            posisi = alphabhet.index(char) - 13
            if posisi < 0:
                # Bungkus ke akhir abjad jika posisi negatif
                hasil += alphabhet[26 + posisi]
            else:
                hasil += alphabhet[posisi]
        else:
            # Jika karakter bukan huruf abjad dibiarkan tidak berubah
            hasil += char
    return hasil


def main():
    # Ambil input dari user
    user_input = input("Enter the text : ")
    # Enkripsi input user
    encrypt_text = encrypt(user_input)
    # Dekripsi teks yang sudah di enkripsi
    decrypt_text = decrypt(encrypt_text)

    # Output Program
    print("Encrypt text : " + encrypt_text)
    print("Decrypt text : " + decrypt_text)


if __name__ == "__main__":
    main()
