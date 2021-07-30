#! /usr/local/bin/python3
# -*- coding: utf-8 -*-


from PIL import Image

from pathlib import Path

imgs_list = []
imgs_path = Path("download_images")

for img in imgs_path.iterdir():
    if img.suffix in ['.jpg','.png']:
        tmp_img = Image.open(img)
        imgs_list.append(tmp_img.convert('RGB'))

img1 = imgs_list.pop(0)

img1.save("imgs.pdf",save_all = True, append_images = imgs_list)

