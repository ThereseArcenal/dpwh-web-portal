import qrcode
import os
from qrcode.constants import ERROR_CORRECT_H

# Your Vercel URL
url = "https://dpwh-web-portal.vercel.app"

# Create folder if it doesn't exist
os.makedirs("static/qrcodes", exist_ok=True)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

# Create image with DPWH colors
img = qr.make_image(fill_color="#1e1e2f", back_color="white")

# Save it (overwrite the old one)
img.save("static/qrcodes/qr-code.png")
print("✅ New QR code generated with Vercel URL!")