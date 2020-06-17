from utils import get_image_url, increment
from urllib.error import HTTPError
from skimage import io
import numpy as np
import sys
import cv2

i = 1
try:
    # Read current image from file, 
    # pick up from where it was last stopped
    with open('currentImage.txt') as f:     
       im = f.read().strip()
    while True:
        # Read image from url
        try:
            url = get_image_url(f'{im}')
            image = io.imread(url)

            # Load classifier  
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            # Black and white image to save compute power
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect if image has a face
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )

            # If faces are found, write image (colour) to file
            if (len(faces) > 0):
                cv2.imwrite(f'images/{im}.png', image)
        except FileNotFoundError:
            print(f'{i}. no image found in {im}')
        finally:
            try:
                # Print number of faces found
                print (f'{i}. found {len(faces)} faces in {im}...')
            except NameError:
                pass
            im = increment(im)
            i += 1

except (KeyboardInterrupt, HTTPError) as e:
    # Write current image to file, before exiting
    with open('currentImage.txt', 'w') as f:
        f.write(f'{im}')
    print(f'Exception {e} was encountered @ {im}\n Exiting...')
    sys.exit(0)
