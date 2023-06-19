# THINGS NEEDED:
#   input: encode/decode, message, path to image
#   output: new image with encoded message 

import os
import functions
import argparse
import numpy as np
import copy
import PIL as pl
from PIL import Image


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

parser.add_argument('-i', type=str, required=True, help='Full path to the image')

group.add_argument('-d', action='store_true', help='Decode messages')

group.add_argument('-e', action='store_true', help='Encode messages')
parser.add_argument('-m', type=str, required=True, help='Message to encode')
parser.add_argument('-n', type=str, help='Name for output file')

args = parser.parse_args()


def main():

    if args.e:
        print("Encrypting\n")
        if (args.m):

            #handles error if file does not exist
            try:
                image = Image.open(args.i)

            except FileNotFoundError:
                print("ERROR: Image file does not exist")
                exit(1)

            
            # prep for encryption
            data_of_image = np.asarray(image)
            message_bin = functions.encode_bin(args.m)
            code = ''.join(message_bin)

            encoded_data = functions.encode_message(data_of_image, code)

            new_img = Image.fromarray(encoded_data)

            if args.n:
                print("Image created: "+args.n)
                new_img.save(str(args.n)+".png")
                
            else:
                print("Image created: encoded_image.png")
                new_img.save("encoded_image.png")
                

    
    elif args.d:
        print("decrypting")
        exit(0)

    exit(0)

main()
# image = Image.open('python/stegonagraphy/picutre-4.png') #Desired image path here

# # convert image into data array 
# data = np.asarray(image)




# # code to get ascii chracters into binary as an array
# code_array = functions.encode_bin("Hello World!")


# #code_array combined into a string
# code = ''.join(code_array)



# original_array = functions.encode_message(data, code)







