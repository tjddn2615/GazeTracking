"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import numpy as np
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    width = 500
    height = 500
    bpp = 3


    if gaze.is_window_8():
        text = "window_8"
        cv2.rectangle(frame, (400, 440),  (800, 660), (0, 0, 255), 3)
    elif gaze.is_window_2():
        text = "window_2"
        cv2.rectangle(frame, (400, 0),  (800, 220), (0, 0, 255), 3)
    elif gaze.is_window_5():
        text = "window_5"
        cv2.rectangle(frame, (400, 220),  (800, 440), (0, 0, 255), 3)
    elif gaze.is_window_7():
        text = "window_7"
        cv2.rectangle(frame, (800, 440),  (1200, 660), (0, 0, 255), 3)
    elif gaze.is_window_9():
        text = "window_9"
        cv2.rectangle(frame, (0, 440),  (400, 660), (0, 0, 255), 3)
    elif gaze.is_window_1():
        text = "window_1"
        cv2.rectangle(frame, (800, 0),  (1200, 220), (0, 0, 255), 3)
    elif gaze.is_window_3():
        text = "window_3"
        cv2.rectangle(frame, (0, 0),  (400, 220), (0, 0, 255), 3)
    elif gaze.is_window_4():
        text = "window_4"
        cv2.rectangle(frame, (800, 220),  (1200, 440), (0, 0, 255), 3)
    elif gaze.is_window_6():
        text = "window_6"
        cv2.rectangle(frame, (0, 220),  (400, 440), (0, 0, 255), 3)
    

    
    
    # if gaze.is_window_1():
    #     text = "window_1"
    #     cv2.rectangle(frame, (800, 0),  (1200, 220), (0, 0, 255), 3)
    # elif gaze.is_window_2():
    #     text = "window_2"
    #     cv2.rectangle(frame, (400, 0),  (800, 220), (0, 0, 255), 3)
    # elif gaze.is_window_3():
    #     text = "window_3"
    #     cv2.rectangle(frame, (0, 0),  (400, 220), (0, 0, 255), 3)
    # elif gaze.is_window_4():
    #     text = "window_4"
    #     cv2.rectangle(frame, (800, 220),  (1200, 440), (0, 0, 255), 3)
    # elif gaze.is_window_5():
    #     text = "window_5"
    #     cv2.rectangle(frame, (400, 220),  (800, 440), (0, 0, 255), 3)
    # elif gaze.is_window_6():
    #     text = "window_6"
    #     cv2.rectangle(frame, (0, 220),  (400, 440), (0, 0, 255), 3)
    # elif gaze.is_window_7():
    #     text = "window_7"
    #     cv2.rectangle(frame, (800, 440),  (1200, 660), (0, 0, 255), 3)
    # elif gaze.is_window_8():
    #     text = "window_8"
    #     cv2.rectangle(frame, (400, 440),  (800, 660), (0, 0, 255), 3)
    # elif gaze.is_window_9():
    #     text = "window_9"
    #     cv2.rectangle(frame, (0, 440),  (400, 660), (0, 0, 255), 3)

    # if gaze.is_blinking():
    #     text = "Blinking"
    # elif gaze.is_right():
    #     text = "Looking right"
    # elif gaze.is_left():
    #     text = "Looking left"
    # elif gaze.is_up():
    #     text = "Looking up"
    # elif gaze.is_down():
    #     text = "Looking down"
    # elif gaze.is_center():
    #     text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()

    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)


    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
