import requests
from bs4 import BeautifulSoup
import os

# URL of the page to scrape
url = 'https://www.louiezong.com/#/bgs/'
#url = input("Entrez l'URL du site Web : ")

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <img> tags in the HTML content
images = soup.find_all('img')

# Path to the folder where images will be saved
folder_path = 'D:\Chôm\Ecole\projets\web scraping\miam_miam'
#folder_path = input("Entrez l'emplacement du dossier où vous souhaitez enregistrer les images : ")


# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop through each <img> tag
for image in images:
    # Check if the <img> tag has a 'src' attribute
    if 'src' not in image.attrs:
        continue

    # Get the URL of the image from the 'src' attribute
    image_url = image['src']

    # Check if the URL starts with 'http' or 'https'
    if not image_url.startswith('http'):
        # If it doesn't, add 'https:' to the beginning of the URL
        image_url = f'https:{image_url}'

    # Extract the filename from the URL and remove any query string
    image_name = os.path.basename(image_url.split('?')[0])

    # Create the full path to save the image to
    image_path = os.path.join(folder_path, image_name)

    # Download and save the image to disk
    with open(image_path, 'wb') as f:
        f.write(requests.get(image_url).content)

