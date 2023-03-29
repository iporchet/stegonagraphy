import os
import functions
import numpy as np
import copy
import PIL as pl
from PIL import Image
    
image = Image.open('python/stegonagraphy/picutre-4.png') #Desired image path here

# convert image into data array 
data = np.asarray(image)

# create copy of data array to compare
data0 = copy.deepcopy(data)

# code to get ascii chracters into binary as string
code = ''.join(functions.encode_bin("Hello World!"))

functions.encode_message(data, code)


if os.path.exists('python/stegonagraphy/new-picture.png') == False:
    new_img = Image.fromarray(data)
    new_img.save("new-picture.png")


image1 = Image.open('new-picture.png') #Desired image path here
data1 = np.asarray(image1)


print("\n")
functions.extract_message(data1)

