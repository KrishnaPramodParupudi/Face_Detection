# Import necessary things
from PIL import Image
import face_recognition

# Load image
image = face_recognition.load_image_file('/home/krishnapramod/Projects/TheFace/Face_Detection/Images/Avengers.jpg')

# Finding face locations
face_locations = face_recognition.face_locations(image)

# Iterating through face_location to seperate and display faces in image
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

''' *** Key Points ***
1. The face_locations is a list of tuples (Each tuple represents a face)
2. Length of all tuples is four
3. The elements in tuple represent the four boarders of a face(top, left, bottom, right)'''
