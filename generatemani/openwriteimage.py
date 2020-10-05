from PIL import Image,ImageDraw,ImageFont
from os import path

from pathFile import dirname,dirnameLogo,filenameimage,filenamelogo




def image():
    try: # FileNotFoundError, OSError, IOError
        pathImage = path.join(dirname, filenameimage)  # join folder and filename
        image = Image.open(pathImage)  # open image

        draw = ImageDraw.Draw(image)
        fontStyle = ImageFont.truetype('Ubuntu-R.ttf', 35)
    except FileNotFoundError:
        print("Exception FileNotFoundError")
    except OSError:
        print("Exception OSError")
    except IOError:
        print("Exception IOError")
    else:
        name = "TIAHA DOUA KEI FRANCK"
        draw.text(xy=(800, 600), text=name, fill=(0, 0, 0), font=fontStyle)
        image.show()




def enterImag(): # upload image
    pass

def enterName(): # enter le nom diplomé
    pass #input("Entrez le nom du diplomé > ")




#https://note.nkmk.me/en/python-pillow-paste/