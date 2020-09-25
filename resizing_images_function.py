import os
from PIL import Image
import glob


image_list = []
resized_images = []


# Following function will search into the picture's folder, will resized it and it will stores en the new picture's folder

def searching_img():
    for pictures in glob.glob('originals\*.jpeg'):
        img = Image.open(pictures)
        image_list.append(img)

        for image in image_list:
            image.thumbnail((2400, 2400))
            # width, height = image.size
            # image = image.resize((int(width / 2), int(height / 2)))
            resized_images.append(image)

            for (i, new) in enumerate(resized_images):
                new.save('{}{}{}'.format(
                    'resized_pictures\picture', i+1, '.png'))


searching_img()


image_list.clear()
resized_images.clear()
