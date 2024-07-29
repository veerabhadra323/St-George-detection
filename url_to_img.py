import pandas as pd
import requests
import os

# Specify the path to your CSV file and the directory where images will be saved
csv_file_path = 'csv files/georges.csv'
save_directory = 'Dataset/georges'

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Read the CSV file
urls = pd.read_csv(csv_file_path, header=None)[0].tolist()

for i, url in enumerate(urls):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Extract the filename from the URL
        filename = os.path.join(save_directory, f'george_{i+1}.jpg')

        # Save the image to the specified directory
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded {filename}")

    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
