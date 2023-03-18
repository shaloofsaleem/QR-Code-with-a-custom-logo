# importing Library
import qrcode
from PIL import Image

#Logo Setup  uploading Image
Logo_link = 'data/logo.jpeg'
logo = Image.open(Logo_link)
# resizing Image
basewidth = 75 # size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth,hsize), Image.LANCZOS)
qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
# Setting the url Link
url='Your link'
qr_big.add_data(url)
qr_big.make()
# QRCode setting Color
img_qr_big = qr_big.make_image(fill_color='#0b4e39', black_color="white").convert('RGB')
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
#saving Qrcode
img_qr_big.save('QRCode.jpg')