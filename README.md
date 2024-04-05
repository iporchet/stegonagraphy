# Stegonagraphy

This program takes plain text as input and encodes it into a new png file. It can then decode that image and retrieve the data. I'm planning on adding more functionality to make it user friendly
and to be able to handle more complex messages and encryptions



## Usage and commands

This program takes in several command line arguments as input. They are the following:
 ```
  -h, --help  show this help message and exit
  -i I        Full path to the image
  -d          Decode messages
  -e          Encode messages
  -m M        Message to encode
  -n N        Name for the output file
```

### Encoding
Encoding messages is done by converting a string's characters into ASCII hex codes. Then the RGB values  

To encode a message, the following flags are required in addition to `-e`: `-i`, `-m`. Optional arguments are: `-n`.

### Decoding 
Decoding the message is similar to encoding the message. By iterating over pixel values and performing a modulo operation on each one, you will end up with a value between 0-15 in hex. This continues until the delimiter appears. Once discovered, the hex codes are converted to ASCII and the message is printed.

To decode a message, the following flags are required in addition to `-d`: `-i`.

>This program only works with images encoded using this program. Other forms of encryption may not work and can cause the program to throw an error.

## Installation 
Not there yet. I want to add more functionality to the program before having it ready as an executable.
