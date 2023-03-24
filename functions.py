def encode_bin(text):
    """Encondes binary message"""
    charsintext = [x for x in text]
    binary_codes = [bin(ord(character))[2:] for character in charsintext]
    
    binary_codes.append(bin(ord(';'))[2:])
    
    return binary_codes



def decode_bin(array_of_bin):
    """Decodes binary message"""
    ascii_codes = [int(str(x), 2) for x in array_of_bin if x != bin(ord(';'))[2:]]
    characters = [chr(x) for x in ascii_codes]

    return ''.join(characters)

def encode_message(data_array, bin_code):

    code_indx = 0

    for x in range(0, len(data_array)):
        for y in range(0, len(data_array[x])):
            if code_indx == len(bin_code):
                break

            else:
                for value in range(0, len(data_array[x][y])):
                    if int(bin_code[code_indx]) != (data_array[x][y][value]%2):
                        data_array[x][y][value] -= 1
                        code_indx += 1

                    else:
                        code_indx += 1
        break
