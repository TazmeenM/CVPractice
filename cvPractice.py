import cv2
import numpy

lower_colour_boundary = numpy.array([0, 100, 100])
upper_colour_boundary = numpy.array([43, 255, 255])

lower_red = numpy.array([0, 100, 100])
upper_red = numpy.array([43, 255, 255])

lower_yellow = numpy.array([43, 100, 100])
upper_yellow = numpy.array([86, 255, 255])

lower_blue = numpy.array([86, 100, 100])
upper_blue = numpy.array([129, 255, 255])

cap = cv2.VideoCapture(0)

while (True):
    
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_colour_boundary, upper_colour_boundary)

    red_counter = 0
    yellow_counter = 0
    blue_counter = 0
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    k = cv2.waitKey(5)

    if (k == 27):
        break

    cv2.imshow("Window", mask)
    for i in red_mask:
        if (red_mask[i].any()):
            red_counter += 1

    for i in yellow_mask:
        if (yellow_mask[i].any()):
            yellow_counter += 1
    
    for i in blue_mask:
        if (blue_mask[i].any()):
            blue_counter += 1

    if (red_counter == yellow_counter == blue_counter):
        print("all")
        break
    elif (red_counter > yellow_counter):
        if (red_counter > blue_counter):
            print("red")
            cv2.imshow("Red", red_mask)
        elif (blue_counter > red_counter):
            print("blue")
            cv2.imshow("Blue", blue_mask)
        else:
            print("red and blue")
            cv2.imshow("Red", red_mask)
            cv2.imshow("Blue", blue_mask)
    elif (yellow_counter > red_counter):
        if (yellow_counter > blue_counter):
            print("yellow")
            cv2.imshow("Yellow", yellow_mask)
        elif (blue_counter > yellow_counter):
            print("blue")
            cv2.imshow("Blue", blue_mask)
        else:
            print("yellow and blue")
            cv2.imshow("Yellow", yellow_mask)
            cv2.imshow("Blue", blue_mask)
    else:
        print("blue")
    