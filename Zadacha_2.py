#Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его.

print('1. Шифрование.')
print('2. Дешифрование.\n')
input_action = int(input('Введите номер действия: '))
input_text = input('Введите текст: ')
input_key = int(input('Введите шаг шифрования: '))
print()

# Функция шифрования
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): #проверить, является ли символ прописным
            c_index = ord(c) - ord('А')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 32 + ord('А')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-32)
            c_index = ord(c) - ord('а')
            c_shifted = (c_index + key) % 32 + ord('а')
            c_new = chr(c_shifted)
            encrypted += c_new
       
        else:
            # если нет алфавита оставьте все как есть
            encrypted += c
    return encrypted

# Функция дешифрования
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('А')
            # сдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 32 + ord('А')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('а')
            c_og_pos = (c_index - key) % 32 + ord('а')
            c_og = chr(c_og_pos)
            decrypted += c_og
        
        else:
            # если нет алфавита, оставьте все как есть
            decrypted += c
    return decrypted    

result = ''

#Шифровка
if input_action == 1: result = cipher_encrypt(input_text,input_key)

#дешифровка
if input_action == 2: result = cipher_decrypt(input_text,input_key)

print(result)    

    