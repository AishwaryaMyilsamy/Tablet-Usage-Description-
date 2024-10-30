from flask import Flask, request, render_template
from tablet_scraper import scrape_tablet_description
from yolo_training import predict_tablet_name
import os

app = Flask('tablet_description')
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        # Save file
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)
        
        # Predict tablet name
        tablet_name = predict_tablet_name(image_path)
        
        # Scrape tablet description
        description = scrape_tablet_description(tablet_name)
        
        return render_template('result.html', tablet_name=tablet_name, description=description)
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
