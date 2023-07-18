import face_recognition
import cv2
import numpy as np
import Controller as cnt
import os


video_capture = cv2.VideoCapture(0)

pasi_image = face_recognition.load_image_file("pasi.jpg")
pasi_encoding = face_recognition.face_encodings(pasi_image)[0]

laki_image = face_recognition.load_image_file("laki.jpg")
laki_encoding = face_recognition.face_encodings(laki_image)[0]


known_face_encoding = [
pasi_encoding,
laki_encoding,

]

known_faces_names = [
"Pasindu",
"Lakindu",

]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True


while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    cnt.systemCondition(1)
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2

                cv2.putText(frame,name+' Recognized',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
                cnt.doorCondition(1)
            else:
                cnt.doorCondition(0)

    cv2.imshow("Face Recognized Door Lock System",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()