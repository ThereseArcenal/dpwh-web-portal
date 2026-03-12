import qrcode
import os
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H

# Your Vercel URL
url = "https://dpwh-web-portal.vercel.app"

print(f"🔧 Generating QR code: qr-code-dpwh.png")

# Make sure folders exist
os.makedirs("static/qrcodes", exist_ok=True)

try:
    # Create QR code
    qr = qrcode.QRCode(
        version=5,
        box_size=10,
        border=4,
        error_correction=ERROR_CORRECT_H
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Generate image
    qr_img = qr.make_image(fill_color="#1e1e2f", back_color="white").convert('RGB')

    # Try to add logo if you have one
    logo_path = "static/images/dpwh-logo.jpg"  # Note: .jpg not .png
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            # Calculate logo size (max 30% of QR code)
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width // 3, 80)
            
            logo = logo.resize((logo_size, logo_size))
            
            pos_x = (qr_width - logo_size) // 2
            pos_y = (qr_height - logo_size) // 2
            
            # Create a white background for the logo
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            # Create a mask
            mask = Image.new('L', (logo_size, logo_size), 0)
            from PIL import ImageDraw
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, logo_size, logo_size), fill=255)
            
            # Paste with circular mask
            qr_img.paste(logo, (pos_x, pos_y), mask)
            print("✅ Logo added successfully")
        except Exception as e:
            print(f"⚠️ Could not add logo: {e}")
    else:
        print(f"⚠️ Logo not found at {logo_path}, creating QR without logo")

    # Save with your custom filename
    qr_img.save("static/qrcodes/qr-code-dpwh.png")
    print(f"✅ Saved as: static/qrcodes/qr-code-dpwh.png")

    # Also save a copy in root
    qr_img.save("qr-code-dpwh.png")
    print(f"✅ Also saved as: qr-code-dpwh.png")

    # Show file size
    file_size = os.path.getsize("static/qrcodes/qr-code-dpwh.png")
    print(f"📊 File size: {file_size} bytes")

    print("🎉 Done! Your QR code is ready with custom name!")

except Exception as e:
    print(f"❌ Error: {e}")