
import qrcode.image.svg
import qrcode

def qrcodegen(data,color_fill,color_back):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=4,
        box_size=10
    )
    url_data = data #"https://validate_diplome.com"

    color_fill = color_fill #"black"
    color_back =color_back #"white"
    qr.add_data(url_data)
    qr.make(fit=True)
    image = qr.make_image(fill=color_fill, black_color=color_back)

    return image