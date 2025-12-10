from PIL import Image
from collections import Counter

def quantize_color(pixel, delta):
    r, g, b = pixel
    return (
        (r // delta) * delta,
        (g // delta) * delta,
        (b // delta) * delta
    )

def extract_top_colors(image_path, top_n=10, delta=20):
    img = Image.open(image_path)
    img = img.resize((200, 200))

    pixels = list(img.getdata())

    # Quantize pixels
    quantized_pixels = [quantize_color(p, delta) for p in pixels]

    counter = Counter(quantized_pixels)
    top_colors = counter.most_common(top_n)

    # Return SIMPLE structure: [(rgb, count), (rgb, count), ...]
    return top_colors
