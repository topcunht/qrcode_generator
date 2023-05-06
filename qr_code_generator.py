import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10, #you can change the size
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "orange", back_color = "white") #choose a color
    img.save("qrimage.png")#name can be changed 

url = input("Enter your URL: ")
generate_qrcode(url)#enter the target link 