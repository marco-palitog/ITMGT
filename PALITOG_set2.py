def shift_letter(letter, shift):
    alphabet_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    else:
        old_order = alphabet_list.find(letter)
        
        new_order = old_order + shift
        if new_order >= 26:
            new_order = (new_order % 26)
        shifted_letter = alphabet_list[new_order]
        return shifted_letter

def caesar_cipher(message, shift):
    alphabet_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    coded_message = ""

    for letter in message:
        if letter == " ":
            coded_message += " "
        else:
            old_order = alphabet_list.find(letter)
            
            new_order = old_order + shift
            if new_order >= 26:
                new_order = (new_order % 26)
            shifted_letter = alphabet_list[new_order]
            coded_message += shifted_letter
    return coded_message

def shift_by_letter(letter, letter_shift):
    alphabet_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = alphabet_list.find(letter_shift)
    if letter == " ":
        return " "
    else:
        old_order = alphabet_list.find(letter)
        
        new_order = old_order + shift
        if new_order >= 26:
            new_order = (new_order % 26)
        shifted_letter = alphabet_list[new_order]
        return shifted_letter

def vigenere_cipher(message, key):
    alphabet_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while len(message) > len(key):
        key += key
    new_key = key[:len(message)]
    new_message = ""
    for char in range(len(message)):
        if message[char] == " ":
            new_message += " "
        else:
            shift = alphabet_list.find(key[char])
            old_order = alphabet_list.find(message[char])
            
            new_order = old_order + shift
            if new_order >= 26:
                new_order = (new_order % 26)
            shifted_letter = alphabet_list[new_order]
            new_message += shifted_letter
    return new_message

def scytale_cipher(message, shift):
    scytale_message = ""
    while len(message) % shift > 0 :
        message += "_"
    for i in range(len(message)):
        scytale_message += message[(i // shift) + (len(message) // shift) * (i % shift)]
    return(scytale_message)

def scytale_decipher(message, shift):
    deciphered_message = ""
    for i in range(len(message)):
        deciphered_message += message[(i % (len(message) // shift)) * shift + ( i // (len(message) // shift))]
    return(deciphered_message)