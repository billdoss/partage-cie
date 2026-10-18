"""Dessine l'icône (éclair sur fond bleu) et l'écrit en PNG. Usage : python3 scripts/make_icons.py"""
from PIL import Image, ImageDraw
import os

BLUE = (31, 79, 216, 255)
AMBER = (255, 200, 87, 255)
BOLT = [(0.57, 0.12), (0.27, 0.56), (0.47, 0.56), (0.41, 0.88), (0.73, 0.43), (0.53, 0.43)]

def draw(size, shape, scale=1.0):
    S = size * 4
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if shape == "square":
        d.rectangle([0, 0, S, S], fill=BLUE)
    elif shape == "rounded":
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=BLUE)
    elif shape == "circle":
        d.ellipse([0, 0, S - 1, S - 1], fill=BLUE)
    pts = [((0.5 + (x - 0.5) * scale) * S, (0.5 + (y - 0.5) * scale) * S) for x, y in BOLT]
    d.polygon(pts, fill=AMBER)
    return img.resize((size, size), Image.LANCZOS)

def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "www", "icons")
    save(draw(192, "rounded"), os.path.join(root, "icon-192.png"))
    save(draw(512, "rounded"), os.path.join(root, "icon-512.png"))
    save(draw(512, "square", 0.72), os.path.join(root, "icon-maskable-512.png"))
    print("icônes écrites dans", os.path.normpath(root))
