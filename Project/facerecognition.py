import facerecognition

# Load the jpg files into numpy arrays
biden_image = facerecognition.load_image_file("Joe Biden.jpg")
obama_image = facerecognition.load_image_file("Barack Obama.jpg")
unknown_image = facerecognition.load_image_file("unknown.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    biden_face_encoding = facerecognition.face_encodings(biden_image)[0]
    obama_face_encoding = facerecognition.face_encodings(obama_image)[0]
    unknown_face_encoding = facerecognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = facerecognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))