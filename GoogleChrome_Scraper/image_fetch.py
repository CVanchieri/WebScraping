### imports ### 
from selenium import webdriver
import time

### function to fetch images from google search ### 
def fetch_image(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd): # function to scroll window
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions) # set sleep time
    ### set the google query url ### 
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    ### get the url query ###
    wd.get(search_url.format(q=query))
    image_urls = set() # creat a dict   
    image_count = 0 # starter count 
    results_start = 0 # result count 
    while image_count < max_links_to_fetch: 
        scroll_to_end(wd) # scroll while count is under 
        ### get thumbnail images from results ###
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results) # how many results 
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        ### click each thumbnail to get actual image ### 
        for img in thumbnail_results[results_start:number_results]:
            try:
                img.click() # click 
                time.sleep(sleep_between_interactions) # set sleep 
            except Exception:
                continue
            ### get the image urls ###
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src')) # add image to image urls
            image_count = len(image_urls) # get count 
            if len(image_urls) >= max_links_to_fetch: # if count is done 
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30) # sleep 
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd") # load more 
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();") # query again 
        results_start = len(thumbnail_results) # set the start further down 

    return image_urls