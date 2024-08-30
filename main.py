import cv2
import gradio as gr
import numpy as np

import cv2
import gradio as gr
import numpy as np

def process_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if not ret:
        cap.release()
        return np.zeros((512, 512, 3), dtype=np.uint8)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    cap.release()
    return edges_bgr

iface = gr.Interface(
    fn=process_frame, 
    inputs=[], 
    outputs="image", 
    live=True, 
    title="Real-Time Edge Detection",
    description="This application captures frames from the webcam and applies edge detection."
)

iface.launch()

