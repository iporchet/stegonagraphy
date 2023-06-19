def encode_bin(text):
    """Encondes binary message"""
    charsintext = [x for x in text]
    binary_codes = [bin(ord(character))[2:] for character in charsintext]
    binary_codes.append(bin(ord(';'))[2:])

    for code in range(len(binary_codes)):
        if len(binary_codes[code]) == 6:
            binary_codes[code] = '0'+binary_codes[code]

    return binary_codes


def decode_bin(array_of_bin):
    """Decodes binary message"""
    ascii_codes = [int(str(x), 2) for x in array_of_bin if x != bin(ord(';'))[2:]]
    characters = [chr(x) for x in ascii_codes]

    return ''.join(characters)


def encode_message(data_array, bin_code):

   
    for digit in range(len(bin_code)):
        for x in range(0, len(data_array)):
            for y in range(0, len(data_array[x])):
                for value in range(0, len(data_array[x][y])):
                    if int(bin_code[digit]) != (data_array[x][y][value]%2):
                        data_array[x][y][value] -= 1
                        break
                    
                break
            break

    return data_array


def extract_message(data_array):
    """Function returns a list of binary codes"""
    binary_array = []
    bit_string = ""

    for row in range(len(data_array)):
        for col in range(len(data_array[row])):
            for channel in range(len(data_array[row][col])):
                if '0111011' == bit_string or '0111011' in binary_array:
                    binary_array.append(bit_string)
                    break

                if len(bit_string) == 7:
                    binary_array.append(bit_string)
                    bit_string = ""
                    bit_string += str(data_array[row][col][channel]%2)

                else:
                    bit_string += str(data_array[row][col][channel]%2)


    return binary_array



