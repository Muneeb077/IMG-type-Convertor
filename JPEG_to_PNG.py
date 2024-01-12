#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:54:29 2023

@author: Muneeb Ur Rehman
"""

import sys
import os
from PIL import Image

    
# grab first and second arguments

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if the new_pics folder exits if not then create the new_pics folder

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print('Already exist')
    

# loop through the entire folder
# convert the JPEG into PNG
# save them into the new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    