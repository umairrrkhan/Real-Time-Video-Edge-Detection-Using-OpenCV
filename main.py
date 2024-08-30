import gradio as gr
import cv2
import numpy as np

def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return edges_bgr
interface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=gr.Image(type="numpy", label="Edges Detected"),
    title="Real-Time Edge Detection",
    description="Upload an image to detect edges using Canny Edge Detection."
)

interface.launch()
