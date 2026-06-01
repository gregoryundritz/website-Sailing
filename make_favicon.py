from PIL import Image
import sys
import os

def process_logo():
    img_path = "./site/img/Logo bleu.png"
    try:
        img = Image.open(img_path).convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)
        
    width, height = img.size
    max_dim = max(width, height)
    
    # Pad to square instead of crop
    img_square = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
    left = (max_dim - width) // 2
    top = (max_dim - height) // 2
    img_square.paste(img, (left, top))
    
    # Save favicons
    img_square.resize((32, 32), Image.Resampling.LANCZOS).save("./site/favicon.ico")
    img_square.resize((180, 180), Image.Resampling.LANCZOS).save("./site/apple-touch-icon.png")
    img_square.resize((192, 192), Image.Resampling.LANCZOS).save("./site/icon-192.png")
    img_square.resize((512, 512), Image.Resampling.LANCZOS).save("./site/icon-512.png")
    print("Favicons created successfully from Logo bleu.png")

    # Create solid white version
    # Take alpha channel
    alpha = img.getchannel('A')
    # Create solid white RGB
    white_img = Image.new("RGB", (width, height), (255, 255, 255))
    # Put alpha back
    white_img.putalpha(alpha)
    
    white_img.save("./site/img/logo-vn-white.png")
    print("White logo created successfully")

if __name__ == '__main__':
    process_logo()
