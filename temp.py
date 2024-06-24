import cv2

# Path to the video file
video_path = 'media/demo.mov'
# Path to save the extracted frame
output_image_path = 'media/preview.png'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
for _ in range(5):
    ret, frame = cap.read()

# Check if the frame was read successfully
if ret:
    # Save the frame as an image
    cv2.imwrite(output_image_path, frame)
    print(f"First frame extracted and saved as {output_image_path}")
else:
    print("Error: Could not read the frame.")

# Release the video capture object
cap.release()
