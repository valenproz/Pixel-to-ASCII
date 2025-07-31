from PIL import Image

def load_and_preprocess_image(magik):
    """Load image and convert to grayscale with resizing."""
    img = Image.open(r"C:\Users\onlin\Downloads\magik.jpg").convert('L')
    return img.resize((img.width // 2, img.height // 2))

def create_brightness_mapping():
    """Create mapping between brightness values and ASCII characters."""
    return {
        'thresholds': [160, 130, 100, 70, 40, 25, 10, 5, 0],
        'chars': [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    }

def generate_ascii_art(image, mapping):
    """Convert image pixels to ASCII characters based on brightness."""
    ascii_art = []
    thresholds, chars = mapping['thresholds'], mapping['chars']
    
    for y in range(image.height):
        row = ''.join(
            chars[next(i for i, t in enumerate(thresholds) if image.getpixel((x, y)) >= t)]
            for x in range(image.width)
        )
        ascii_art.append(row)
    return ascii_art

def save_ascii_art(ascii_art, output_file):
    """Save ASCII art to text file."""
    with open(output_file, 'w') as f:
        f.write('\n'.join(ascii_art))

def main():
    # Configuration
    IMAGE_PATH = "C:/Users/onlin/Downloads/magik.jpg"
    OUTPUT_FILE = "C:/Users/onlin/Downloads/ascii_image.txt"
    
    # Generate ASCII art
    image = load_and_preprocess_image(IMAGE_PATH)
    mapping = create_brightness_mapping()
    ascii_art = generate_ascii_art(image, mapping)
    save_ascii_art(ascii_art, OUTPUT_FILE)

if __name__ == "__main__":
    main()