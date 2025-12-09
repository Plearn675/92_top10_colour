from collections import Counter
from PIL import Image

def extract_top_colors(image_path, top_n=10):
    img = Image.open(image_path)
    img = img.resize((200, 200))  # speed optimization
    pixels = list(img.getdata())

    counter = Counter(pixels)
    return counter.most_common(top_n)
