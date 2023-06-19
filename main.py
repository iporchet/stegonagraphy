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
group.add_argument('-e', type=str, action='store_true', help='Encode messages')
group.add_argument('-d', type=str, required=True, help='Decode messages')

parser.add_argument('-m', type=str, required=True, help='Message to encode')
parser.add_argument('-i', type=str, required=True, help='Path to the image')
parser.add_argument('--name', type=str, help='Name for output file')
args = parser.parse_args()


def main():
    pass

# image = Image.open('python/stegonagraphy/picutre-4.png') #Desired image path here

# # convert image into data array 
# data = np.asarray(image)




# # code to get ascii chracters into binary as an array
# code_array = functions.encode_bin("Hello World!")


# #code_array combined into a string
# code = ''.join(code_array)



# original_array = functions.encode_message(data, code)







