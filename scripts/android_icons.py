"""Remplace l'icône par défaut du projet Android (appelé par le workflow GitHub après `cap add android`)."""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_icons import draw, save

res = os.path.join("android", "app", "src", "main", "res")
shutil.rmtree(os.path.join(res, "mipmap-anydpi-v26"), ignore_errors=True)
for name, px in [("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)]:
    d = os.path.join(res, "mipmap-" + name)
    save(draw(px, "rounded"), os.path.join(d, "ic_launcher.png"))
    save(draw(px, "circle"), os.path.join(d, "ic_launcher_round.png"))
    save(draw(px, "rounded"), os.path.join(d, "ic_launcher_foreground.png"))
print("icônes Android remplacées")
