"""
small code to remove the background of a python image

"""
__author__ = "TIAHA DOUA KEI FRANCK"

from PIL import Image
import numpy as np
from os import path
from pathLogo import dirnameLogo,filenameLogo

def deletebackgroundlogo():

    try :
        imagePath = path.join(dirnameLogo,filenameLogo)
        imageOpen = Image.open(imagePath).convert('RGBA')

        x = np.array(imageOpen)
        r,g,b,a = np.rollaxis(x, axis=-1)

        r[a == 0] = 255
        b[a == 0] = 255
        g[a == 0] = 255

        x = np.dstack([r,b,g,a])
        imageOpen = Image.fromarray(x,'RGBA')


    except FileNotFoundError:
        print("Exception FileNotFoundError")
    except OSError:
        print("Exception OSError")
    except IOError:
        print("Exception IOError")
    else:
        imageOpen.show()
        #small code to remove the background of a python image
        #imageOpen.save('fp','/tmp/out.jpg')
    finally:
        print(__author__)

