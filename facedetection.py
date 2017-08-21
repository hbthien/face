'''
Created on Aug 8, 2017

@author: hoang
'''

#Face detection using lib 'face_recognition'

from PIL import Image
import face_recognition


# Load the jpg file into a numpy array
image = face_recognition.load_image_file("/home/hoang/Downloads/Chuongtrinhnguon/git/face_recognition/examples/unknown/images7.jpeg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)
print(face_locations)

print("Found {} face(s)".format(len(face_locations)))

# pil_images = []
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face: Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    im  = Image.fromarray(face_image)
    im.show()
#     pil_images.append(im)
# 
# if len(pil_images)>0:
#     for im in pil_images:
#         im.show() 


