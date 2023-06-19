import os
import functions
import numpy as np
import copy
import PIL as pl
from PIL import Image
    
image = Image.open('python/stegonagraphy/picutre-4.png') #Desired image path here

# convert image into data array 
data = np.asarray(image)

x = 'hello'

# create copy of data array to compare
data0 = copy.deepcopy(data)

# code to get ascii chracters into binary as an array
code_array = functions.encode_bin("Hello World!")


#code_array combined into a string
code = ''.join(code_array)

total = 0
for x in code:
    total += 1
    print(total)


original_array = functions.encode_message(data, code)


if os.path.exists('python/stegonagraphy/new-picture.png') == False:
    new_img = Image.fromarray(data)
    new_img.save("new-picture.png")


image1 = Image.open('new-picture.png') #Desired image path here
data1 = np.asarray(image1)

print(data1)

print(functions.extract_message(data1))

