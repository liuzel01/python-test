import requests
from urllib.request import urlretrieve
from pathlib import Path
import ssl

"""
下载图片的三种方式
"""

def urllib_download(img_url, download_path):
    ssl._create_default_https_context = ssl._create_unverified_context # 不校验ssl
    urlretrieve(img_url, download_path)


def request_download(img_url, download_path):
    r = requests.get(img_url)
    with open(download_path, 'wb') as f:
        f.write(r.content)


def requests_chunk_download(img_url, download_path):
    r = requests.get(img_url, stream=True)
    with open(download_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

if __name__ == '__main__':
    img_url = 'https://img1.baidu.com/it/u=2825220054,2215241009&fm=26&fmt=auto&gp=0.jpg'
    download_path = Path('./download_images')
    download_path.mkdir(exist_ok=True)
    urllib_download(img_url,f"{download_path}/images1.jpg")
    request_download(img_url, f"{download_path}/images2.jpg")
    requests_chunk_download(img_url, f"{download_path}/images3.jpg")