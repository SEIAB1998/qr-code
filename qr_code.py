pip install qrcode

from PIL import image 
data ="https://exemple.com"

qr=qrcode.QRcode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=true)
image=qr.make_image(fill="black",back_color="white")

image.save("qr_code.png")
Image.open("qr_code.png")
