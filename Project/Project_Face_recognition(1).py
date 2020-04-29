import facerecognition
image=facerecognition.load_image_file("biden.jpg")
face_locations=facerecognition.face_locations(image)
face_landmarks_list=facerecognition.face_landmarks(image)
known_image = facerecognition.load_image_file("biden.jpg")
unknown_image = facerecognition.load_image_file("unknown.jpg")


biden_encoding = facerecognition.face_encodings(known_image)[0]
unknown_encoding = facerecognition.face_encodings(unknown_image)[0]

results = facerecognition.compare_faces([biden_encoding], unknown_encoding)
face_locations = facerecognition.face_locations(image, model="cnn")
results = facerecognition.compare_faces([my_face_encoding], unknown_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")