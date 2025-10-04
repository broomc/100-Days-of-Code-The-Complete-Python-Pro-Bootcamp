from PIL import Image
import os

for i in range(100):
    ps_file = f"frame_{i:03d}.ps"
    png_file = f"frame_{i:03d}.png"
    img = Image.open(ps_file)
    img.save(png_file)
    
png_files = sorted([
    f for f in os.listdir()
    if f.lower().endswith('.png')
])

frames = [Image.open(f) for f in png_files]

frames[0].save(
    'output.gif',
    format='GIF',
    save_all=True,
    append_images=frames[1:],
    duration=10,  # milliseconds per frame
    )