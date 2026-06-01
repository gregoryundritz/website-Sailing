from PIL import Image
import sys

def process_image():
    img_path = "./site/img/Logo bleu.png"
    img = Image.open(img_path).convert("RGBA")
    
    width, height = img.size
    
    # We will create two new images:
    # 1. Transparent blue logo (for favicons)
    # 2. Solid white logo (for header)
    
    blue_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    white_img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    
    pixels = img.load()
    blue_pixels = blue_img.load()
    white_pixels = white_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Difference between max and min channel
            c_max = max(r, g, b)
            c_min = min(r, g, b)
            diff = c_max - c_min
            
            # The blue logo is around (26, 109, 237) -> diff = 211
            # Grey checkerboard is around (54,54,54) or (112,112,112) -> diff close to 0
            
            # Smooth step for alpha
            low = 10
            high = 60
            
            if diff <= low:
                alpha = 0
            elif diff >= high:
                alpha = 255
            else:
                alpha = int(255 * (diff - low) / (high - low))
                
            # For the blue logo, we keep the original color but apply our computed alpha
            # Wait, if we keep the original color, the edge pixels might have grey mixed in.
            # Let's just force the color to the target blue if it has some alpha, 
            # or just use the original color since it's anti-aliased.
            # To remove the dark grey from the edges, we can boost the color based on the target blue
            # Actually, standard un-premultiply is hard because we don't know which grey it blended with.
            # Let's just use the original color and it will be mostly fine.
            blue_pixels[x, y] = (r, g, b, alpha)
            
            # For the white logo, we use solid white and the same alpha
            white_pixels[x, y] = (255, 255, 255, alpha)
            
    blue_img.save("./site/img/logo-bleu-transparent.png")
    white_img.save("./site/img/logo-vn-white.png")
    print("Images saved.")
    
    # Also regenerate favicons
    max_dim = max(width, height)
    
    # Pad to square instead of crop
    img_square = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
    left = (max_dim - width) // 2
    top = (max_dim - height) // 2
    img_square.paste(blue_img, (left, top))
    
    img_square.resize((32, 32), Image.Resampling.LANCZOS).save("./site/favicon.ico")
    img_square.resize((180, 180), Image.Resampling.LANCZOS).save("./site/apple-touch-icon.png")
    img_square.resize((192, 192), Image.Resampling.LANCZOS).save("./site/icon-192.png")
    img_square.resize((512, 512), Image.Resampling.LANCZOS).save("./site/icon-512.png")
    print("Favicons updated.")

if __name__ == '__main__':
    process_image()
