from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(img, text):
    img = Image.open(img)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', size=30)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 200, height - 40), text, font=myfont, fill=fillcolor)
    return img

def add_img_watermark(img, img_watermark):
    rgba_image = Image.open(img).convert("RGBA")
    rgba_watermark = Image.open(img_watermark).convert("RGBA")
    image_x, image_y = rgba_image.size
    watermark_x, watermark_y = rgba_watermark.size
    # 缩放图片
    scale = 10
    watermark_scale = max(image_x / (scale * watermark_x), image_y / (scale * watermark_y))
    new_size = (int(watermark_x * watermark_scale), int(watermark_y * watermark_scale))
    rgba_watermark = rgba_watermark.resize(new_size, resample=Image.ANTIALIAS)
    # 透明度
    rgba_watermark_mask = rgba_watermark.convert("L").point(lambda x: min(x, 180))
    rgba_watermark.putalpha(rgba_watermark_mask)

    watermark_x, watermark_y = rgba_watermark.size
    # 水印位置
    rgba_image.paste(rgba_watermark, ( (image_x - watermark_x)//2, image_y - watermark_y-5))  # 右上角

    return rgba_image.convert("RGB")


if __name__ == '__main__':
    image = './download_images/images1.jpg'
    img1 = add_text_watermark(image,'@Python七号')
    img1.save("./download_images/result_text_watermark.jpg","jpeg")

    img_watermark = "./download_images/logo.jpg"
    img2 = add_img_watermark(image, img_watermark)
    img2.save("./download_images/result_img_watermark.jpg")