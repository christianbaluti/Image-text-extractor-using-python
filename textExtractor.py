!pip install pytesseract
!sudo apt install tesseract-ocr
!pip install opencv-python

import cv2
import pytesseract

# Mount Google Drive to access images if needed
from google.colab import drive
drive.mount('/content/drive')

def scrape_text_from_image(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply some preprocessing to improve the accuracy of OCR
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(gray)

    return text

# Provide the path to the image you want to scrape text from
image_path = "/content/drive/MyDrive/path_to_your_image.jpg"

# Scrape text from the image
extracted_text = scrape_text_from_image(image_path)

print("Extracted Text:")
print(extracted_text)
