
from PIL import Image

key = 50

img = Image.open("1.png")
pixels = img.load()

width, height = img.size


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[i, j] = (r, g, b)

img.save("encrypted_image.jpg")

print("Image Encrypted Successfully!")


img = Image.open("encrypted_image.jpg")
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels[i, j] = (r, g, b)

img.save("decrypted_image.jpg")

print("Image Decrypted Successfully!")
