import qrcode
import os
from qrcode.constants import ERROR_CORRECT_H

# YOUR CORRECT VERCEL URL
url = "https://dpwh-web-portal.vercel.app"

print(f"🔧 Generating QR code for: {url}")

# Make sure the folder exists
os.makedirs("static/qrcodes", exist_ok=True)

# Generate new QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

# Create image with your brand colors
img = qr.make_image(fill_color="#1e1e2f", back_color="white")

# Save to static folder (for your website)
img.save("static/qrcodes/qr-code.png")
print(f"✅ Saved to: static/qrcodes/qr-code.png")

# Also save a copy in current folder
img.save("qr-code.png")
print(f"✅ Saved to: qr-code.png (current folder)")

print("🎉 DONE! Your QR code now points to your Vercel URL!")