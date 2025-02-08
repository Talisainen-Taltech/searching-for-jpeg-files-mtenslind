#!/usr/bin/env python

import os
import requests
from zipfile import ZipFile
# Download the zipfile
download_url = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"

request = requests.get(download_url)
with open("random_files.zip", "wb") as zipfile:
    zipfile.write(request.content)

# extract the zipfile
with ZipFile("random_files.zip", 'r') as zip:
    zip.extractall()
# Rename jpegs with correct extensions
jpeg_signature = bytes([0xFF, 0xD8])
directory = r'random_files'

for name in os.listdir(directory):
    file_path = os.path.join(directory, name)
    with open(file_path, 'rb') as file:
        magic_num = file.read(2)

        if magic_num.startswith(jpeg_signature) and name.endswith(".jpg") == False:
            new_file = os.path.join(directory, name + ".jpg")
            os.rename(file_path, new_file)



