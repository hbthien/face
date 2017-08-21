'''
Created on Aug 9, 2017

#Face detection using lib 'dlib'

@author: hoang
'''


import sys
import dlib
from skimage import io

file_name = '/home/hoang/Downloads/Chuongtrinhnguon/git/face_recognition/examples/unknown/images7.jpeg'#sys.argv[1]

# Create a HOG face detector obj by using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

# Load the image into an array
image = io.imread(file_name)

# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the faces in our image.
detected_faces = face_detector(image, 1)

print("Found {} faces in the file {}".format(len(detected_faces), file_name))

# Open a window on the desktop showing the image
win.set_image(image)

# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):

    # Detected faces are returned as an object with the coordinates 
    # of the top, left, right and bottom edges
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

    # Draw a box around each face we found
    win.add_overlay(face_rect)
            
# Wait until the user hits <enter> to close the window            
dlib.hit_enter_to_continue()


