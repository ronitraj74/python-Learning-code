import qrcode

url = input("Enter the URL here: ").strip()
file_path = "C:\\Users\\iamro\\OneDrive\\Documents\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")