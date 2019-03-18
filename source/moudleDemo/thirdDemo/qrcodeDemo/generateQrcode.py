#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 13:31
# @Author  : li_panfeng
# @File    : generateQrcode.py
# @Software: PyCharm
# @context : 生成二维码

import qrcode
from MyQR import myqr
from source.utils.creator import create_queue_name as cqn

NAME = cqn('test.png')


def simple():
    """简单用法"""
    img = qrcode.make('hello, qrcode')
    img.save(NAME)


def advanced():
    """
    参数含义：
        version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。
                 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

        error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
        ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
        ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
        ROR_CORRECT_H：大约30%或更少的错误能被纠正。

        box_size：控制二维码中每个小格子包含的像素数。

        border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('hello, qrcode')
    qr.make(fit=True)
    img = qr.make_image()
    img.save(NAME)


# 个性二维码 需要用到myqr
def myqrDemo():
    """
    参数  	    含义      	    详细
    word	    二维码指向链接	str， 输入链接或者句子作为参数
    version	    边长	            int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级
    level	    纠错等级	        str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为’H’
    picture	    结合图片	        str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
    colorized	颜色	            bool，使产生的图片由黑白变为彩色的
    contrast	对比度	        float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    brightness	亮度	            float，调节图片的亮度，其余用法和取值与 contrast 相同
    save_name	输出文件名	    str，默认输出文件名是”qrcode.png”
    save_dir	存储位置	        str，默认存储位置是当前目录

    """
    # myqr.run('https://www.baidu.com')
    # myqr.run('https://www.baidu.com', save_name=NAME)
    myqr.run('wo shi ni da ye', 20, 'Q', 'dog.png', True, 0.2, 0.9, NAME)

def effect2():
    """黑白 点状"""
    myqr.run(
        words='https://www.baidu.com',
        picture="dog.png",
        save_name=NAME
    )

def effect3():
    myqr.run(
        words='https://www.baidu.com',
        picture="dog.png",
        colorized=True,
        save_name=NAME
    )

if __name__ == '__main__':
    simple()
    advanced()
    myqrDemo()
    effect2()
    effect3()
    pass
