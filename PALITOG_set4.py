def bin_to_dec(binary_string):
    digits = len(binary_string) - 1
    decimal = 0
    for place_value in range(digits  + 1):
        decimal += int(binary_string[digits - place_value]) * (2 ** place_value)
    return(decimal)

def dec_to_bin(number):
    binary_string = str(number % 2)
    floor_quotient = number // 2
    while floor_quotient > 0:
        binary_string += str(floor_quotient % 2)
        floor_quotient = floor_quotient // 2
    binary_string = binary_string[::-1]
    #remove zeroes at the start
    binary_int = int(binary_string)
    binary_string = str(binary_int)
    return(binary_string)

def telephone_cipher(message):
    message_list = []
    message_list = list(message)
    for character in range(len(message_list)):
        message_list[character] = encoder_dict.get(message_list[character])

    #add underscores
    for character in range(len(message_list) - 1):
        if message_list[character][0] == message_list[character + 1][0]:
            message_list[character] += "_"

    #combine list to string
    cipher_message = ""
    for character in range(len(message_list)):
        cipher_message += message_list[character]

    return(cipher_message)


def telephone_decipher(telephone_string):
    conversion_string = telephone_string[0]
    
    for character in range(1, len(telephone_string)):
        if telephone_string[character] != telephone_string[character - 1]:
            conversion_string += "_"
            conversion_string += telephone_string[character]
        else:
            conversion_string += telephone_string[character]
            
    telephone_list = conversion_string.split("_")
    #cleans the list of blanks
    for code in range(len(telephone_list)):
        if len(telephone_list[code]) == 0:
            telephone_list[code] = "*"
    for iterations in range(telephone_list.count("*")):
        telephone_list.remove("*")

    #converts
    for code in range(len(telephone_list)):
        telephone_list[code] = decipher_dict.get(telephone_list[code])

    #combine
    deciphered_message = ""
    for letter in range(len(telephone_list)):
        deciphered_message += telephone_list[letter]

    return(deciphered_message)
    
'''
Given Dictionary for Set 4
'''
encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }