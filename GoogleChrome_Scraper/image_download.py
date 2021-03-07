### imports ### 
import requests
import os, io , hashlib
from PIL import Image

### function to download an image ###
def download_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content # get content from url request
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}") # exception
    try:
        image_file = io.BytesIO(image_content) # convert contests to bytes
        image = Image.open(image_file).convert('RGB') # convert image to RGB
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg') # create a file path for the image 
        with open(file_path, 'wb') as f: # open the file path   
            image.save(f, "JPEG", quality=85) # save the image 
        print(f"SUCCESS - saved {url} - as {file_path}") # success
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}") # exception