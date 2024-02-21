from PIL import Image

def main():
    print("""\n
    _                              _                         _ _
    (_)_ __ ___   __ _  __ _  ___  | |_ ___     __ _ ___  ___(_|_)
    | | '_ ` _ \ / _` |/ _` |/ _ \ | __/ _ \   / _` / __|/ __| | |
    | | | | | | | (_| | (_| |  __/ | || (_) | | (_| \__ \ (__| | |
    |_|_| |_| |_|\__,_|\__, |\___|  \__\___/   \__,_|___/\___|_|_|
    __ _  ___ _ __   |___/ __ __ _| |_ ___  _ __                
    / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|               
    | (_| |  __/ | | |  __/ | | (_| | || (_) | |                  
    \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|                  
    |___/                                                        
    \n""")

    path=input("Which image do you want to use? (Enter path to image): \n")

    try:
        img=Image.open(path)
    except:
        print(path, "File not found.")

    # resize, grayscale, get pixels into ascii array, get length
    ascii_str = make_ascii(grayscale(resize(img)))
    total_pixels = len(ascii_str)
    new_width = 100 # fit to screen
    result = "\n".join(ascii_str[i:(i+new_width)] for i in range(0, total_pixels, new_width))
    
    #print
    print(result)

    #save
    open("result.txt", "w").write(result);



# ARRAY: define ascii art to be used for img (11 elements, 0-10)
ASCII_ARR = ["@", "#", "8", "1", "x", "/", ";", ",", ".", "^", "`"]

# FUNC MAKE_ASCII: turns pixels into ascii
def make_ascii(img):
    pixels = img.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_ARR[pixel//25];
    return ascii_str

# FUNC GRAYSCALE
def grayscale(img):
    return img.convert("L")

# FUNC RESIZE: make img fit in terminal
def resize(img, new_width = 100):
    w, h = img.size
    ratio = h / w / 2.1 #bc height is abt 1.65x bigger than width
    new_height = int(new_width * ratio)
    resized_img = img.resize((new_width, new_height))
    return resized_img

main()