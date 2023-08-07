import cv2 as cv


def resizeFrame(frame, rate=0.25):
    
    width = int(frame.shape[1]*rate)
    height = int(frame.shape[0]*rate)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_LINEAR)

path = 'Images/sample2.mp4'
capture = cv.VideoCapture(path)

fps = 60
delay = int(1000/fps)

while True:
    isTrue, frame = capture.read()
    
    newFrame = resizeFrame(frame)
    cv.imshow('Video', newFrame)
    
    if cv.waitKey(delay) & 0xFF==ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()