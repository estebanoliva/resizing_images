from PIL import Image

# image = Image.open('Listing 16 Nuevo\IMG_0633.jpeg')
# image.show()


image = Image.open('originals\IMG_0639.jpeg')
image.thumbnail((2400, 2400))
image.save('image_thumbnail.png')

print(image.size)  # Output: (400, 258)
