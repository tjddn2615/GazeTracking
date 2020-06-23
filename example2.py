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

    right_cnt=0
    left_cnt=0
    center_cnt=0
    text=""

    if faces:
        for face in faces:

            #if face:
                #print("face found")

            gaze.refresh(frame, face)

            frame = gaze.annotated_frame()


            if gaze.is_blinking():
                text = "Blinking"
            elif gaze.is_right():
                text = "Looking right"
                right_cnt+=1
            elif gaze.is_left():
                text = "Looking left"
                left_cnt+=1
            elif gaze.is_center():
                text = "Looking center"
                center_cnt+=1
            #elif gaze.is_up():
            #    text = "Looking up"
            #elif gaze.is_down():
            #    text = "Looking down"

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()

            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)

        if(right_cnt>=left_cnt and right_cnt>=center_cnt):
            cv2.rectangle(frame, (0, 0),  (640, 1080), (0, 0, 255), 3)
            text = "Looking right"
        elif(left_cnt>=right_cnt and left_cnt>=center_cnt):
            cv2.rectangle(frame, (1280, 0),  (1920, 1080), (0, 0, 255), 3)
            text = "Looking left"
        elif(center_cnt>=right_cnt and center_cnt>=left_cnt):
            cv2.rectangle(frame, (640, 0),  (1280, 1080), (0, 0, 255), 3)
            text = "Looking center"
    else:
        gaze.refresh(frame,None)
        frame = gaze.annotated_frame()


    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.imshow("Demo", frame)


    if cv2.waitKey(1) == 27:
        break
