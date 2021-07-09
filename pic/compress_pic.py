import tinify
from pathlib import Path
import os

tinify.key = '此处填入你的key'
path = "./download_images" # 图片存放的路径

for dirpath, dirs, files in os.walk(path):
    for file in files:
        file = Path(dirpath)/Path(file)
        if file.suffix.lower() in ['.jpg','.png','.gif']:
            print("compressing ..."+ file.as_posix())
            tinify.from_file(file.as_posix()).to_file(file.with_suffix(".compressed.jpg").as_posix())
