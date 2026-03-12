import qrcode
import os
from qrcode.constants import ERROR_CORRECT_H

# Your website URL - use your actual IP
url = "http://192.168.1.3:5000"

# Create qrcodes folder if it doesn't exist
os.makedirs("static/qrcodes", exist_ok=True)

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

# Generate image with your DPWH colors
img = qr.make_image(fill_color="#333446", back_color="white")

# Save as qr-code.png in static/qrcodes folder (MATCHES YOUR HTML)
filepath = "static/qrcodes/qr-code.png"
img.save(filepath)
print(f"✅ QR Code saved to {filepath}")

# Also save a copy in the current directory for easy access
img.save("qr-code.png")
print("✅ Also saved as qr-code.png in current folder")