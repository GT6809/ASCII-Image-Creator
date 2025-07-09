from PIL import Image
import os

ascii_chars = ['@', '$', '#', '%', ' ']
image_path = "logo.png"

try:
    img = Image.open(image_path).convert("RGBA")
except Exception as e:
    print(f"Erreur : {e}")
    input("Appuie sur Entrée pour quitter.")
    exit(1)

scale_x = 0.5
scale_y = 0.25

img = img.resize((int(img.width * scale_x), int(img.height * scale_y)))

ascii_output = ""
for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = img.getpixel((x, y))
        if a == 0:
            ascii_output += " "
        else:
            luminosity = 0.299 * r + 0.587 * g + 0.114 * b
            index = int((luminosity / 255) * (len(ascii_chars) - 1))
            index = (len(ascii_chars) - 1) - index
            ascii_output += ascii_chars[index]
    ascii_output += "\n"

with open("ascii_output.txt", "w", encoding="utf-8") as f:
    f.write(ascii_output)

print("ASCII généré dans 'ascii_output.txt'")
input("Appuie sur Entrée pour l'ouvrir...")

os.system("notepad ascii_output.txt")
