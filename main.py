import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0) # 0 indicate the the one camera if we have 2 we can use it 2 okay 

while True:
    # Read a frame from the webcam 
    ret, frame = cap.read()
    
    # Check if frame was read correctly
    if not ret:
        print("Error reading frame")
        break
        
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # the image or the video will be convert here into gray
    
    # Apply some processing
    edges = cv2.Canny(gray, 100, 200)   # canny so it what do it find the edges in the frame 
    
    # Convert back to BGR for display
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) 
    
    # Display result
    cv2.imshow('frame', edges)
    
    # Break if ESC key pressed
    if cv2.waitKey(1) == 27:
        break
        
# Release the webcam
cap.release()
cv2.destroyAllWindows()