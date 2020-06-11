"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import dlib
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    #print("in")
    
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(frame2)

    if faces:
        for face in faces:

            #if face:
                #print("face found")

            gaze.refresh(frame, face)

            frame = gaze.annotated_frame()
            text=""


            if gaze.is_blinking():
                text = "Blinking"
            elif gaze.is_right():
                text = "Looking right"
            elif gaze.is_left():
                text = "Looking left"
            elif gaze.is_up():
                text = "Looking up"
            elif gaze.is_down():
                text = "Looking down"
            elif gaze.is_center():
                text = "Looking center"

            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()

            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

            cv2.imshow("Demo", frame)
    else:
        gaze.refresh(frame,None)
        frame = gaze.annotated_frame()
        cv2.imshow("Demo", frame)


    if cv2.waitKey(1) == 27:
        break
