from PIL import Image
import sys

def create_favicons():
    img_path = "./site/img/IMG_6794.jpeg"
    try:
        img = Image.open(img_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)
        
    # Crop to a square centered
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    
    img_square = img.crop((left, top, right, bottom))
    
    # Save favicons
    img_square.resize((32, 32), Image.Resampling.LANCZOS).save("./site/favicon.ico")
    img_square.resize((180, 180), Image.Resampling.LANCZOS).save("./site/apple-touch-icon.png")
    img_square.resize((192, 192), Image.Resampling.LANCZOS).save("./site/icon-192.png")
    img_square.resize((512, 512), Image.Resampling.LANCZOS).save("./site/icon-512.png")
    print("Favicons created successfully")

if __name__ == '__main__':
    create_favicons()
