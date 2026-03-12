import qrcode
import os

print("🔧 Testing QR code generation...")

# Create folder
os.makedirs("static/qrcodes", exist_ok=True)

# Simple QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://dpwh-web-portal.vercel.app")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("static/qrcodes/test-qr.png")

print("✅ Test QR code saved!")