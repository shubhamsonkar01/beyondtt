import os
import sys

try:
    from PIL import Image
except ImportError:
    print("PILLOW_NOT_FOUND")
    sys.exit(0)

def compress_image(path):
    if "_low." in path: return # ignore already compressed
    base, ext = os.path.splitext(path)
    if ext.lower() not in ['.png', '.jpg', '.jpeg']: return
    
    out_path = base + "_low.jpg"
    try:
        img = Image.open(path).convert('RGB')
        # Resize if width > 800
        if img.width > 800:
            ratio = 800.0 / img.width
            img = img.resize((800, int(img.height * ratio)), Image.Resampling.LANCZOS)
        
        # Save as high-compression JPEG
        img.save(out_path, "JPEG", optimize=True, quality=40)
        print(f"Compressed {path} -> {os.path.getsize(path)//1024}KB to {os.path.getsize(out_path)//1024}KB")
    except Exception as e:
        print(f"Failed {path}: {e}")

# Walk dirs
for root, dirs, files in os.walk('.'):
    for n in dirs:
        if n.startswith('.'): dirs.remove(n) # skip hidden
    for f in files:
        compress_image(os.path.join(root, f))
print("DONE_COMPRESSING")
