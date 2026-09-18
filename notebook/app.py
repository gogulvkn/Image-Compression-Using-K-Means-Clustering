import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_image(image_path, output_path, k=16):
    # Load and convert image to RGB
    image = Image.open(image_path).convert("RGB")
    img_array = np.array(image)
    
    height, width, channels = img_array.shape
    pixels = img_array.reshape(-1, 3)
    
    # K-Means Clustering
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixels)
    
    # Map pixels to cluster centers
    centers = np.uint8(kmeans.cluster_centers_)
    compressed_pixel = centers[kmeans.labels_]
    compressed_image = compressed_pixel.reshape(height, width, 3)
    
    # Save the processed image
    Image.fromarray(compressed_image).save(output_path, quality=70)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['image']
        if file.filename == '':
            return "No selected file", 400
            
        k_clusters = int(request.form.get('k_clusters', 16))
        
        if file:
            # Save original upload
            orig_filename = file.filename
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], orig_filename)
            file.save(input_path)
            
            # Process and save compressed version
            comp_filename = f"compressed_{orig_filename}"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], comp_filename)
            
            process_image(input_path, output_path, k=k_clusters)
            
            return render_template(
                'index.html',
                original_image=input_path,
                compressed_image=output_path,
                k_value=k_clusters
            )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)