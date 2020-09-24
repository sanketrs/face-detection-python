from cv2 import cv2

print("Hello World ")

# print the open-cv version
print(cv2.__version__)


# Load the cascade classfier
face_cascade = cv2.CascadeClassifier("face-detector.xml")

# Read the input image
img = cv2.imread('Capture.png')


# Detect faces in the image
faces = face_cascade.detectMultiScale(
    img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)


# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Export the resultant image
cv2.imwrite("detect_result.png", img)
print('Successfully Saved')
