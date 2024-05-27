# mycode.py
alphabhet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(text):
    text = text.lower()
    hasil = ''
    for char in text:
        if char.isalpha():
            hasil += alphabhet[(alphabhet.index(char) + 13) % 26]
        else:
            hasil += char
    return hasil


def decrypt(text):
    text = text.lower()
    hasil = ''
    for char in text:
        if char.isalpha():
            posisi = alphabhet.index(char) - 13
            if posisi < 0:
                hasil += alphabhet[26 + posisi]
            else:
                hasil += alphabhet[posisi]
        else:
            hasil += char
    return hasil
