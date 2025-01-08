import cv2
import os
import time

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened properly
if cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Convert the frame to RGB color space
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Set the directory where the image will be saved
        directory = "D:\honeypot\pythonProject\Honeypot-Implementation\images"

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create a unique filename using the current timestamp
        timestamp = int(time.time())  # Get the current time in seconds
        filename = f"Intruder_{timestamp}.jpg"  # Add timestamp to the filename

        # Save the image
        full_path = os.path.join(directory, filename)
        cv2.imwrite(full_path, cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))  # Convert back to BGR for saving
        print(f"Image saved as {filename} in {directory}")
    else:
        print("Failed to capture image.")
else:
    print("Failed to open webcam.")

# Release the webcam
cap.release()
