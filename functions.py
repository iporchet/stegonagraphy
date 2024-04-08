class Image_encoder:
    def __init__(self, data_array, stringmssge=""):
        self.data_array = data_array
        self.mssge = stringmssge
        self.hex_string = ""
 

    def encode_hex(self):
        """Encodes hex message"""
        charsintext = [x for x in self.mssge]
        hex_codes = [hex(ord(character))[2:] for character in charsintext]
        hex_codes.append(hex(ord(';'))[2:])
        self.hex_string = ''.join(hex_codes)

    def decode_hex(self):
        ascii_array = []

        for index in range(0, len(self.hex_string), 2):
            ascii_array.append(chr(int(self.hex_string[index]+self.hex_string[index+1], 16)))

        self.hex_string = ''.join(ascii_array[:len(ascii_array)-1])

    def encode_message_hex(self):   
        digit = 0


        for x in range(0, len(self.data_array)):
            for y in range(0, len(self.data_array[x])):
                for value in range(0, len(self.data_array[x][y])):

                    #TODO: mod 16 rgb value then add or subtract difference between actual value
                    if digit < len(self.hex_string):
                        if int(self.hex_string[digit], 16) < (self.data_array[x][y][value]%16):
                            self.data_array[x][y][value] -= (self.data_array[x][y][value]%16) - int(self.hex_string, 16)
                            digit += 1

                        elif int(self.hex_string[digit], 16) > (self.data_array[x][y][value]%16):
                            self.data_array[x][y][value] += int(self.hex_string[digit], 16) - (self.data_array[x][y][value]%16)
                            digit += 1

                        else:
                            digit += 1
                    else:
                        return True
    
        return False

    def extract_message_hex(self):
        hex_string = ""

        for row in range(len(self.data_array)):
            for col in range(len(self.data_array[row])):
                for channel in range(len(self.data_array[row][col])):

                    if "3b" in hex_string:
                        return hex_string

                    else:
                        hex_string += str(hex(self.data_array[row][col][channel]%16))[2:]
        
        self.hex_string = hex_string

