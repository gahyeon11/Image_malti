from flask import Flask, request, send_file, render_template, send_from_directory, jsonify, url_for
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)
app = Flask(__name__, instance_path=r'D:\zolzak\Imageone\object', root_path=r'D:\zolzak\Imageone\object')

@app.route('/')
def index():
    return render_template('Imageone.html')

@app.route('/object/<filename>')
def serve_object_image(filename):
    return send_from_directory('object', filename)

@app.route('/get-object-images')
def get_object_images():
    image_files = os.listdir('object')
    object_images = []

    try:
        for filename in image_files:
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join('object', filename)
                with open(image_path, 'rb') as img_file:
                    image_data = img_file.read()
                    no_bg_image = remove(image_data)  # Remove background
                    object_images.append({
                        'url': url_for('serve_object_image', filename=filename, _external=True),
                        'no_bg_url': url_for('serve_no_bg_object_image', filename=filename, _external=True),
                    })
    except Exception as e:
        print(f"Error loading object images: {str(e)}")

    return jsonify(object_images=object_images)  # JSON response
@app.route('/object-no-bg/<filename>')
def serve_no_bg_object_image(filename):
    image_path = os.path.join('object', filename)
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()
        no_bg_image = remove(image_data)  # Remove background
    return send_file(BytesIO(no_bg_image), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
