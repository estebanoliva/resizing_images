from PIL import Image

# image = Image.open('Listing 16 Nuevo\IMG_0633.jpeg')
# image.show()


image = Image.open('originals\IMG_0633.jpeg')
image.thumbnail((1200, 1800))
image.save('image_thumbnail.jpeg')

print(image.size)  # Output: (400, 258)
