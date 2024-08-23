import cv2
import numpy

what_to_do = 0

lower_colour_boundary = numpy.array([37, 100, 100])
upper_colour_boundary = numpy.array([63, 100, 100])

lower_red = numpy.array([0, 100, 100])
upper_red = numpy.array([16, 255, 255])

lower_yellow = numpy.array([51, 100, 100])
upper_yellow = numpy.array([72, 255, 255])

lower_blue = numpy.array([189, 100, 100])
upper_blue = numpy.array([264, 255, 255])

cap = cv2.VideoCapture(0)
_, frame = cap.read()

def fraction_of_frame(number_of_pixels):
    resolution = frame.shape
    total_number_of_pixels = resolution[0] * resolution[1]
    return (number_of_pixels / total_number_of_pixels)

def what_to_do_function():
    what_to_do = 0

def colour_balance(red_counter, yellow_counter, blue_counter):
    if (red_counter == yellow_counter == blue_counter == 0):
        print("black")
    elif (red_counter == yellow_counter == blue_counter != 0):
        print("all")
        return "all"
    elif (red_counter == yellow_counter):
        print("red and yellow")
        #cv2.imshow("Red", red_mask)
        #cv2.imshow("Yellow", yellow_mask)
        return "red and yellow"
    elif (red_counter > yellow_counter):
        if (red_counter > blue_counter):
            print("red")
            #cv2.imshow("Red", red_mask)
            return "blue"
        elif (blue_counter > red_counter):
            print("blue")
            #cv2.imshow("Blue", blue_mask)
            return "blue"
        else:
            print("red and blue")
            #cv2.imshow("Red", red_mask)
            #cv2.imshow("Blue", blue_mask)
            return "red and blue"
    elif (yellow_counter > red_counter):
        if (yellow_counter > blue_counter):
            print("yellow")
            #cv2.imshow("Yellow", yellow_mask)
            return "yellow"
        elif (blue_counter > yellow_counter):
            print("blue")
            #cv2.imshow("Blue", blue_mask)
            return "blue"
        else:
            print("yellow and blue")
            #cv2.imshow("Yellow", yellow_mask)
            #cv2.imshow("Blue", blue_mask)
            return "yellow and blue"
    else:
        print("blue")
        return "blue"
    
    #if (fraction_of_frame(red_counter) > 0.001):
     #   print("Too much red")
    #else:
     #   print("Not enough red")
    
def colour(b, g, r):
    if (g < 128 and b == 0):
        return "red"
    elif (r < 200 and b == 0 and r <= g):
        return "yellow"
    elif (g < 200 and r == 0):
        return "blue"
    else:
        return "blue"

def what_to_do_function(what_to_do):
    lower_colour_boundary = numpy.array([0, 100, 100])
    upper_colour_boundary = numpy.array([43, 255, 255])

    lower_red = numpy.array([0, 100, 100])
    upper_red = numpy.array([43, 255, 255])

    lower_yellow = numpy.array([43, 100, 100])
    upper_yellow = numpy.array([86, 255, 255])

    lower_blue = numpy.array([86, 100, 100])
    upper_blue = numpy.array([129, 255, 255])

    cap = cv2.VideoCapture(0)
    while (what_to_do == 0):
        
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

        #cv2.imshow("Window", mask)
        #for i in red_mask:
         #   if (red_mask[i].any()):
           #     red_counter += 1

        #for i in yellow_mask:
         #   if (yellow_mask[i].any()):
          #      yellow_counter += 1
        
        #for i in blue_mask:
         #   if (blue_mask[i].any()):
          #      blue_counter += 1
        for i in range(480):
            for j in range(640):
                if (colour(frame[i, j][0], frame[i, j][1], frame[i, j][2]) == "red"):
                    red_counter += 1
                elif (colour(frame[i, j][0], frame[i, j][1], frame[i, j][2]) == "yellow"):
                    yellow_counter +=1
                    print(yellow_counter)
                elif (colour(frame[i, j][0], frame[i, j][1], frame[i, j][2]) == "blue"):
                    blue_counter += 1
                

        
        return colour_balance(red_counter, blue_counter, yellow_counter)
        
        if (fraction_of_frame(red_counter) > 0.001):
            print("Too much red")
            #break
        else:
            print("Not enough red")


    while (what_to_do == 1):
        _, frame = cap.read()
        lower_colour_boundary = numpy.array([0, 25, 25])
        upper_colour_boundary = numpy.array([255, 230, 230])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_colour_boundary, upper_colour_boundary)
        k = cv2.waitKey(5)

        if (k == 27):
            break
        
        #cv2.imshow("Window", mask)
        '''
        threshold = cv2.threshold(mask, 100, 255, 0)
        print("before")
        contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print("after")
        contours_drawing = cv2.drawContours(mask, contours, -1, (10, 10, 10), 3)
        cv2.imshow("Contours", contours_drawing)
        '''
