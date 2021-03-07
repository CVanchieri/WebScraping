### imports ### 
from image_fetch import fetch_image
from image_download import download_image
from selenium import webdriver
import os

### searchable info ###
search_term = 'kangaroo' # term to search 
num_images =  50 # number of images want 

### set the driver path from chrome ### 
DRIVER_PATH = '/Users/cvanchieri/Documents/CS/GitHub/Repos/WebScraping/GoogleChrome_Scraper/chromedriver' # set the path to the chromedriver
wd = webdriver.Chrome(executable_path=DRIVER_PATH) # set the webdriver
### function to search the term, create a folder for images, download images ### 
def search_download(search_term:str,driver_path:str,target_path=f'./{search_term}_images',number_images=num_images):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' '))) # create the target folder 
    if not os.path.exists(target_folder): # if the folder doesnt exist  
        os.makedirs(target_folder) # creat a new folder 
    with webdriver.Chrome(executable_path=driver_path) as wd: # using the webdriver 
        res = fetch_image(search_term, number_images, wd=wd, sleep_between_interactions=0.5) # fetch the images from the term
    for elem in res: # for each image 
        download_image(target_folder,elem) # use the download image function 

### run the search function with params ### 
search_download(
                search_term=search_term, # search term 
                driver_path=DRIVER_PATH # driver path 
                )