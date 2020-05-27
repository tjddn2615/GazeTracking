"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
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

    if gaze.is_window_1():
        text = "window_1"
    elif gaze.is_window_2():
        text = "window_2"
    elif gaze.is_window_3():
        text = "window_3"
    elif gaze.is_window_4():
        text = "window_4"
    elif gaze.is_window_5():
        text = "window_5"
    elif gaze.is_window_6():
        text = "window_6"
    elif gaze.is_window_7():
        text = "window_7"
    elif gaze.is_window_8():
        text = "window_8"
    elif gaze.is_window_9():
        text = "window_9"

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
