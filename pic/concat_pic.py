from pathlib import Path

from PIL import Image


def concat_pics(pics:list, image_path:str):
    """
    :param pics: 待拼接的图片路径列表
    :param image_path: 拼接后的图片存放路径
    :return: None
    """
    img_list = []
    for img in pics:
        img_list.append(Image.open(img))

    width = 0
    height = 0
    for img in img_list:
        # 单幅图像尺寸
        w, h = img.size
        height += h
        # 取最大的宽度作为拼接图的宽度
        width = max(width, w)

    # 创建空白长图，这里可以传入 color 设置空白地方的颜色，默认黑色
    result = Image.new(img_list[0].mode, (width, height), color='#ffffff')
    # 拼接图片
    height = 0
    for img in img_list:
        w, h = img.size
        # 图片水平居中
        result.paste(img, box=(round(width / 2 - w / 2), height))
        height += h
    # 保存图片
    result.save(image_path)





if __name__ == '__main__':
    pics = []
    imgs_path = Path('./download_images')
    for img in imgs_path.iterdir():
        if img.suffix.lower() in ['.jpg']:
            pics.append(img.as_posix())
    concat_pics(pics,"./download_images/拼接长图.jpg")