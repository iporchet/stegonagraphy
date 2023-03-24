import os
import functions
import numpy as np
import PIL as pl
from PIL import Image
    
image = Image.open('python/stegonagraphy/picutre-4.png') #Desired image path here
data = np.asarray(image)

# code to get ascii chracters into binary
code = ''.join(functions.encode_bin("Hello World!"))

functions.encode_message(data, code)

print(data)


if os.path.exists('python/stegonagraphy/new-picture.png') == False:
    new_img = Image.fromarray(data)
    new_img.save("new-picture.png")