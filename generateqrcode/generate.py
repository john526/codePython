import qrcode
import qrcode.image.svg
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

def generateqrcode():

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    url_data = "https://github.com/john526"
    name_file = "qrcode1.png"
    color_fill="black"
    color_back = "white"
    qr.add_data(url_data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=color_fill,back_color=color_back)
    image.save(name_file)