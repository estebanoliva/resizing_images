import os
from PIL import Image
import glob


# empty list

image_list = []
resized_images = []

for filename in glob.glob('originals\*.jpeg'):
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    width, height = image.size
    image = image.resize((int(width / 5), int(height / 5)))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('resized_pictures\picture', i+1, '.png'))


image_list.clear()
resized_images.clear()
print(image_list)
print(resized_images)
