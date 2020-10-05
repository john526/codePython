from PIL import Image,ImageFont,ImageDraw,ImageFilter
import numpy as np
from os import path
from pdf417 import render_svg,render_image,encode
import qrcode
import qrcode.image.svg
from pathFile import dirname,dirnameLogo,dirnameQrcode,dirnamePdf417,filenamePdf417,filenameimage,filenamelogo, filenameQrcode,url_data,name_file,color_fill,color_back,filenameSecondePdf417
from deletebackground import deletebackground
from qrcodeGn import qrcodegen
from genpdf417 import genpdf417Func
from message import director

"""
ERROR_CORRECT_L
About 7% or less errors can be corrected.
ERROR_CORRECT_M (default)
About 15% or less errors can be corrected.
ERROR_CORRECT_Q
About 25% or less errors can be corrected.
ERROR_CORRECT_H.
About 30% or less errors can be corrected.
"""

def associateImage():

    try :
        pathImage = path.join(dirname,filenameimage)
        pathLogo = path.join(dirnameLogo,filenamelogo)

        openImage = Image.open(pathImage)
######################################call deletebackground #######################################

        openLogo = deletebackground(pathLogo)

##############################################################################################################

####################################GENERATE QRCODE ##################################################
        image = qrcodegen(url_data,color_fill,color_back)
        image.save(name_file)
        pathQrcode = path.join(dirnameQrcode,filenameQrcode)
        image = deletebackground(pathQrcode)

######################################################################################
########################################GENERATE PDF 471###################################################################
        """codes = encode(director,columns=10,security_level=8)
        renderImage = render_image(codes,ratio=1,scale=2)
        renderImage.save(filenamePdf417)"""
        genpdf417Func(director,filenamePdf417)
        pathPdf417 = path.join(dirnamePdf417,filenamePdf417)
        renderImage = deletebackground(pathPdf417)

        genpdf417Func(director, filenameSecondePdf417)
        pathPdf417 = path.join(dirnamePdf417, filenameSecondePdf417)
        renderImage2 = deletebackground(pathPdf417)

###########################################################################################################
###############################Write name and paste logo and paste qrcode##############################################

        openImage.paste(openLogo,(1570,200)) # paste openLogo on openImage
        openImage.paste(image,(1500,950))#paste qrcode
        openImage.paste(renderImage,(450,900)) # pdf417
        openImage.paste(renderImage2,(1000,900))
        draw = ImageDraw.Draw(openImage) # draw
        name = "TIAHA DOUA KEI FRANCK"
        fontStyle = ImageFont.truetype('Waree-BoldOblique.ttf', 40)
        draw.text(xy=(800,600),font=fontStyle,text=name,fill=(0,0,0))
#############################################################################################################
    except FileNotFoundError:
        print("Exception FileNotFoundError")
    except OSError:
        print("Exception OSError")
    except IOError:
        print("Exception IOError")
    else:
        openImage.show() # show image
    #openLogo.show()


