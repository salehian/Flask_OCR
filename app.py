from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']

    # Read the uploaded file using PIL
    image = Image.open(file.stream)

    # Convert the image to grayscale and apply thresholding
    gray = image.convert('L')
    thresh = gray.point(lambda x: 0 if x < 128 else 255, '1')

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(thresh)

    # Pass the text to the template to display in the browser
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run()