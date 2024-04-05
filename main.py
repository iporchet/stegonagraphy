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
parser.add_argument('-m', type=str, help='Message to encode')
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
                print("ERROR: Image file {args.i} does not exist")
                exit(1)

            
            # prep for encryption
            data_of_image = np.asarray(image)
            encoder = functions.Image_encoder(data_of_image, args.m) 
            encoder.encode_hex()

            if (encode.encode_message_hex()):
                new_img = Image.fromarray(encoded_data)

            if args.n:
                print("Image created: "+args.n)
                new_img.save(str(args.n)+".png")
                
            else:
                print("Image created: encoded_image.png")
                new_img.save("encoded_image.png")
                
    elif args.d:
        print("Decrypting:\n")
        
        try:
            image = Image.open(args.i)

        except FileNotFoundError:
            print("ERROR: Image file {args.i} does not exist")
            exit(1)

        data_of_image = np.asarray(image)
        message_from_array = functions.extract_message_hex(data_of_image)
        print(functions.decode_hex(message_from_array))
        #DEBUGGING
        

    exit(0)

main()
