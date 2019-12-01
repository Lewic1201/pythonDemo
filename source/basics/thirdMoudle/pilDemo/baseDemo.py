import os
import sys
from PIL import Image
from PIL import ImageFilter

"""https://pillow.readthedocs.org/"""

avatar = Image.open('img27.jpg', 'r')
print(avatar.format, avatar.size, avatar.mode)


def trans_format():
    """转换图片格式"""
    for infile in sys.argv[1:]:
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print("cannot convert", infile)


def create_min_image():
    """制作缩略图"""
    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".thumbnail"
        if infile != outfile:
            try:
                im = Image.open(infile)
                x, y = im.size
                im.thumbnail((x // 2, y // 2))
                im.save(outfile, "JPEG")
            except IOError:
                print("cannot create thumbnail for", infile)


def create_img():
    # 通常使用RGB模式就可以了
    new_img = Image.new('RGB', (100, 100), 'red')
    new_img.save("1.jpg", "JPEG")

    new_img = Image.new('RGB', (100, 100), '#B286FF')
    new_img.save("2.jpg", "JPEG")

    new_img = Image.new('RGB', (100, 100), (255, 255, 128))
    new_img.save("3.jpg", "JPEG")


def open_img():
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(BASE_PATH, "fj.jpg")

    # 打开图片
    img = Image.open(file_path)

    """
    format : 识别图像的源格式，如果该文件不是从文件中读取的，则被置为 None 值。
    size : 返回的一个元组，有两个元素，其值为象素意义上的宽和高。
    mode :
    · 1 (1-bit pixels, black and white, stored with one pixel per byte)
    · L (8-bit pixels, black and white)
    · P (8-bit pixels, mapped to any other mode using a colour palette)
    · RGB (3x8-bit pixels, true colour)
    · RGBA (4x8-bit pixels, true colour with transparency mask)
    · CMYK (4x8-bit pixels, colour separation)
    · YCbCr (3x8-bit pixels, colour video format)
    · I (32-bit signed integer pixels)
    · F (32-bit floating point pixels)
    """

    print(img.format, img.size, img.mode, img.height, img.width)
    h, w = img.size  # (X,Y)
    # 等价于
    # h = img.heigth
    # w = img.width

    # 缩略图
    img.thumbnail((w * 0.75, h // 2))
    img.save("1.jpg", "JPEG")

    # 应用模糊滤镜:
    im2 = img.filter(ImageFilter.BLUR)  # 存储图片(使用滤波过滤)
    im2.save('blur.jpg', 'JPEG')
