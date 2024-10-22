import cv2 as cv
from tkinter import *
from tkinter import ttk
import threading

root = Tk()

max_value = 255
low_R = 0
low_G = 0
low_B = 0
high_R = max_value
high_G = max_value
high_B = max_value

window_detection_name = 'Object Detection'

low_R_name = 'Low R'
low_G_name = 'Low G'
low_B_name = 'Low B'
high_R_name = 'High R'
high_G_name = 'High G'
high_B_name = 'High B'

# Accessed with both threads
stop_flag = False

def on_low_R(val):
    global low_R
    low_R = val
    low_R = min(high_R - 1, low_R)
    #cv.setTrackbarPos(low_R_name, window_detection_name, low_R)

def on_high_R(val):
    global high_R
    high_R = val
    high_R = max(high_R, low_R + 1)
    #cv.setTrackbarPos(high_R_name, window_detection_name, high_R)

def on_low_G(val):
    global low_G
    low_G = val
    low_G = min(high_G - 1, low_G)
    #cv.setTrackbarPos(low_G_name, window_detection_name, low_G)

def on_high_G(val):
    global high_G
    high_G = val
    high_G = max(high_G, low_G + 1)
    #cv.setTrackbarPos(high_G_name, window_detection_name, high_G)

def on_low_B(val):
    global low_B
    low_B = val
    low_B = min(high_B - 1, low_B)
    #cv.setTrackbarPos(low_B_name, window_detection_name, low_B)

def on_high_B(val):
    global high_B
    high_B = val
    high_B = max(high_B, low_B + 1)
    #cv.setTrackbarPos(high_B_name, window_detection_name, high_B)

def close_all():
    global stop_flag
    print("Stopping OpenCV and Tkinter...")
    stop_flag = True
    root.quit()

def grab_color():
    global low_R, low_G, low_B, high_R, high_G, high_B
    print(f"{low_R},{low_G},{low_B},{high_R},{high_G},{high_B}")

def set_color(color_label):
    global low_R, low_G, low_B, high_R, high_G, high_B
    if color_label == "red":
        low_R, low_G, low_B = 140, 50, 0
        high_R, high_G, high_B = 255, 105, 130
    elif color_label == "green":
        low_R, low_G, low_B = 0, 130, 200
        high_R, high_G, high_B = 150, 255, 250
    elif color_label == "blue":
        low_R, low_G, low_B = 0, 0, 105
        high_R, high_G, high_B = 75, 95, 255
    else:
        # Default case (reset all)
        low_R, low_G, low_B = 0, 0, 0
        high_R, high_G, high_B = 255, 255, 255

    #update_trackbars()

    print(f"Set color {color_label}: {low_R},{low_G},{low_B},{high_R},{high_G},{high_B}")

def update_trackbars():
    cv.setTrackbarPos(low_R_name, window_detection_name, low_R)
    cv.setTrackbarPos(low_G_name, window_detection_name, low_G)
    cv.setTrackbarPos(low_B_name, window_detection_name, low_B)
    cv.setTrackbarPos(high_R_name, window_detection_name, high_R)
    cv.setTrackbarPos(high_G_name, window_detection_name, high_G)
    cv.setTrackbarPos(high_B_name, window_detection_name, high_B)

def thresholding():
    global stop_flag
    cap = cv.VideoCapture(0)

    cv.namedWindow(window_detection_name)
    cv.createTrackbar(low_R_name, window_detection_name, low_R, max_value, on_low_R)
    cv.createTrackbar(high_R_name, window_detection_name, high_R, max_value, on_high_R)
    cv.createTrackbar(low_G_name, window_detection_name, low_G, max_value, on_low_G)
    cv.createTrackbar(high_G_name, window_detection_name, high_G, max_value, on_high_G)
    cv.createTrackbar(low_B_name, window_detection_name, low_B, max_value, on_low_B)
    cv.createTrackbar(high_B_name, window_detection_name, high_B, max_value, on_high_B)

    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        lower_bound = (low_B, low_G, low_R)
        upper_bound = (high_B, high_G, high_R)
        frame_threshold = cv.inRange(frame, lower_bound, upper_bound)
        masked_frame = cv.bitwise_and(frame, frame, mask=frame_threshold)

        cv.imshow(window_detection_name, masked_frame)

        key = cv.waitKey(30)
        if key == ord('q') or key == 27:
            stop_flag = True
            break
        update_trackbars()

    cap.release()
    cv.destroyAllWindows()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Thresholding with OpenCV").grid(column=0, row=0)
ttk.Button(frm, text="Start", command=lambda: threading.Thread(target=thresholding).start()).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=close_all).grid(column=1, row=1)

ttk.Label(frm, text="RED").grid(column=0, row=2)
ttk.Button(frm, text="Set Red", command=lambda: set_color("red")).grid(column=1, row=2)

ttk.Label(frm, text="GREEN").grid(column=0, row=3)
ttk.Button(frm, text="Set Green", command=lambda: set_color("green")).grid(column=1, row=3)

ttk.Label(frm, text="BLUE").grid(column=0, row=4)
ttk.Button(frm, text="Set Blue", command=lambda: set_color("blue")).grid(column=1, row=4)

root.mainloop()