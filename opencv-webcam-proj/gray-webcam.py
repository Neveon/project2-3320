import cv2

# Object class VideoCapture allows us to get the frames
# from a webcam
capture = cv2.VideoCapture(0)

while(True):
    # read() returns a tuple

    # ret is a Boolean telling us if a frame was given
    # it can be used for error checking

    # frame is a numpy ndarry of the captured image
    ret, frame = capture.read()

    # We then convert the frame to gray
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame in a window
    cv2.imshow("Gray Video", grayFrame)

    cv2.imshow("Normal Video", frame)

    # Spacebar breaks out of the while loop
    if cv2.waitKey(1) == 32:
        break

# "Releases" the camera
capture.release()

# Closes windows
cv2.destroyAllWindows()
