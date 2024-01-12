#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:29:52 2023

@author: muneeburrehman
"""

import sys
import os
from PIL import Image

image = sys.argv[1]
converted_image = sys.argv[2]

if not os.path.exists(converted_image):
    os.makedirs(converted_image)

for filename in os.listdir(image):
    img = Image.open(f'{image}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{converted_image}{clean_name}.tiff','tiff')