import cv2

def resizeFrame(frame, rate=0.75):
    
    width = int(frame.shape[1]*rate)
    height = int(frame.shape[0]*rate)
    
    dimension = (width, height)
    
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_LINEAR)


img = cv2.imread('Images/toy.jpeg')

cv2.imshow('Image', img)
cv2.imshow('Resized Image', resizeFrame(img))

cv2.waitKey(0)
