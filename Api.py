import os
import requests
from PIL import Image
import imagehash

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def calculate_hash(image_path):
    img = Image.open(image_path)
    return str(imagehash.average_hash(img))

def find_matching_image(target_url, folder_path):
    # Download the target image
    target_image_path = 'target_image.jpg'
    download_image(target_url, target_image_path)
    target_hash = calculate_hash(target_image_path)

    # Iterate through images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust the file extensions as needed
            image_path = os.path.join(folder_path, filename)
            image_hash = calculate_hash(image_path)

            # Compare hash values
            if target_hash == image_hash:
                return image_path

    return None

# Example usage



from flask import Flask,request
app = Flask(__name__)

@app.route('/identify', methods = ['POST', 'GET'])
def identify():
    if request.method == 'POST':
        matching_image_path = find_matching_image(request.get_json()['url'], 'balls')

        if matching_image_path:
            print(f"Matching image found: {matching_image_path[6:][:-4]}")
            return matching_image_path[6:][:-4]
        else:
            print("No matching image found.")
            return "Not found"
        
    else:
        return "<h1>U should send a post request to me 😡</h1>";