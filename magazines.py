import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_and_rename_image(args):
    url, folder_name, index = args
    response = requests.get(url, verify=False)  # Disable SSL verification for simplicity
    if response.status_code != 200:
        print(f"Failed to download {url}")
        return

    filename = f"{index:02d}.jpg"  # 01.jpg, 02.jpg, ...
    path = os.path.join(folder_name, filename)

    with open(path, 'wb') as f:
        f.write(response.content)
        print(f"{filename} was downloaded to {folder_name}/")

def scrape_image_links(page_url):
    response = requests.get(page_url, verify=False)  # Disable SSL verification for simplicity
    if response.status_code != 200:
        raise Exception(f"Error loading page: {page_url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')

    image_urls = []
    for img in image_tags:
        src = img.get('src')
        if src:
            full_url = urljoin(page_url, src)
            image_urls.append(full_url)

    return image_urls

def get_folder_name_from_url(url):
    parsed = urlparse(url)
    path_parts = [part for part in parsed.path.split('/') if part]
    folder_name = 'revista_' + '_'.join(path_parts)
    return folder_name

def main():
    start = time.perf_counter()

    revista_url = "https://revisteriaponchito.com/5x/3/"
    folder_name = get_folder_name_from_url(revista_url)

    os.makedirs(folder_name, exist_ok=True)

    image_urls = scrape_image_links(revista_url)
    print(f"Found {len(image_urls)} images in {revista_url}")

    # List of tuples (url, folder_name, index) 
    download_args = [(url, folder_name, i+1) for i, url in enumerate(image_urls)]

    with ThreadPoolExecutor() as executor:
        executor.map(download_and_rename_image, download_args)

    finish = time.perf_counter()
    print(f"It took {finish - start:.2f} second(s) to finish.")

if __name__ == "__main__":
    main()

