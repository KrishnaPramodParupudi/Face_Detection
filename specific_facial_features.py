# Import necessary stuff
# PIL IS Python Image Library
from PIL import Image, ImageDraw
import face_recognition

# Loading Image (Make sure your code and image are in same folder else you have to specify the whole path of image)
image = face_recognition.load_image_file("/home/krishnapramod/Projects/TheFace/Face_Detection/Images/Mahesh.jpg")

# The below code identifies all the faces in a picture and length of the list gives the number of faces(In this case it is one)
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)
print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# To draw on the image
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)


# Iterating through all faces in face_landmarks_list(In this case, only one face)
for face_landmarks in face_landmarks_list:
         d.line(face_landmarks['left_eye'],width=5) # Specifying only the features we want (Both the eyes)
         d.line(face_landmarks['right_eye'],width=5)
pil_image.show()
