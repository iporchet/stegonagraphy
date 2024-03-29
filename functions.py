def encode_hex(text):
    """Encodes hex message"""
    charsintext = [x for x in text]
    hex_codes = [hex(ord(character))[2:] for character in charsintext]
    hex_codes.append(hex(ord(';'))[2:])

    return hex_codes

def decode_hex(hex_string):
    ascii_array = []

    for index in range(0, len(hex_string), 2):
        ascii_array.append(chr(int(hex_string[index]+hex_string[index+1], 16)))

    return ''.join(ascii_array[:len(ascii_array)-1])

def encode_message_hex(data_array, hex_code):
    digit = 0


    for x in range(0, len(data_array)):
        for y in range(0, len(data_array[x])):
            for value in range(0, len(data_array[x][y])):

                #TODO: mod 16 rgb value then add or subtract difference between actual value
                if digit < len(hex_code):
                    if int(hex_code[digit], 16) < (data_array[x][y][value]%16):
                        data_array[x][y][value] -= (data_array[x][y][value]%16) - int(hex_code[digit], 16)
                        digit += 1

                    elif int(hex_code[digit], 16) > (data_array[x][y][value]%16):
                        data_array[x][y][value] += int(hex_code[digit], 16) - (data_array[x][y][value]%16)
                        digit += 1

                    else:
                        digit += 1
                else:
                    return data_array

def extract_message_hex(data_array):
    hex_string = ""

    for row in range(len(data_array)):
        for col in range(len(data_array[row])):
            for channel in range(len(data_array[row][col])):

                if "3b" in hex_string:
                    return hex_string

                else:
                    hex_string += str(hex(data_array[row][col][channel]%16))[2:]


