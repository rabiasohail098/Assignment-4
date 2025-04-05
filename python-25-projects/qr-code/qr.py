import qrcode
import cv2
import numpy as np
from PIL import Image
# Removed unnecessary import of IPython.display

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="white")
    img.save(filename)
    img.show()  # Open the QR code image using the default image viewer
    print(f"✅ QR Code saved as {filename}")

def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        print(f"✅ Decoded Data: {data}")
    else:
        print("❌ No QR code found! Try using a white background.")

generate_qr("Successfully Generated", "my_qr.png")  # Encode
decode_qr("my_qr.png")  # Decode