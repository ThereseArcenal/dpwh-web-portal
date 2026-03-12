import qrcode
import os
from PIL import Image, ImageDraw, ImageFont
from qrcode.constants import ERROR_CORRECT_H

# Your Vercel URL
url = "https://dpwh-web-portal.vercel.app"

print(f"🔧 Generating QR code with text logo for: {url}")

os.makedirs("static/qrcodes", exist_ok=True)

# Create QR code
qr = qrcode.QRCode(
    version=5,
    box_size=10,
    border=4,
    error_correction=ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

# Generate QR code
qr_img = qr.make_image(fill_color="#1e1e2f", back_color="white").convert('RGB')

# Create a small white square in the center for the logo
qr_width, qr_height = qr_img.size
center_size = 60
pos_x = (qr_width - center_size) // 2
pos_y = (qr_height - center_size) // 2

# Draw white rectangle
draw = ImageDraw.Draw(qr_img)
draw.rectangle([pos_x, pos_y, pos_x + center_size, pos_y + center_size], fill="white")

# Add "DPWH" text
try:
    # Try to use a font (might need to adjust path)
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

# Center the text
text = "DPWH"
text_width = len(text) * 12  # rough estimate
text_x = pos_x + (center_size - text_width) // 2
text_y = pos_y + (center_size - 20) // 2

draw.text((text_x, text_y), text, fill="#FB8B23", font=font)

# Save
qr_img.save("static/qrcodes/qr-code-with-logo.png")
qr_img.save("qr-code-with-logo.png")
print("✅ QR code with text logo created!")