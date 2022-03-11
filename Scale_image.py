import cv2
import numpy as np
import os
import xml.dom.minidom
from fractions import Fraction
import fractions

path = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径
fx = 2
fy = 2

# fx1 = fractions.Fraction(fx)  # 将小数转换为分数
# fy1 = fractions.Fraction(fy)
print(path)


def scale_xml():
    indir = path + '/inference/scale/xml'  # xml目录
    outdir = path + '/inference/scale/txt'  # txt目录
    os.chdir(indir)
    xmls = os.listdir('.')
    # categories = {'CV': '0',  # 航母
    #               'LHA': '1',  # 两栖攻击舰
    #               'LSD': '2',  # 船坞登陆舰
    #               'DD': '3',  # 驱逐舰
    #               'SS': '4',  # 潜艇
    #               'PC': '5',  # 小型军舰
    #               'PS': '6',  # 非货船
    #               'CS': '7'}  # 货轮
    categories = {'ship': '0'}
    for i, file in enumerate(xmls):
        print(file)
        file_save = file.split('.')[0] + '_fx_' + str(fx) + '_fy_' + str(fy) + '.txt'
        # file_save = file.split('.')[0] + '.txt'
        file_txt = os.path.join(outdir, file_save)
        f_w = open(file_txt, 'w')
        DOMTree = xml.dom.minidom.parse(file)
        annotation = DOMTree.documentElement

        objects = annotation.getElementsByTagName("object")
        img_width = annotation.getElementsByTagName('width')[0].firstChild.nodeValue
        img_height = annotation.getElementsByTagName('height')[0].firstChild.nodeValue
        print(img_width)
        print(img_height)
        img_depth = annotation.getElementsByTagName('depth')[0].firstChild.nodeValue

        if float(img_width) % float(2) != 0:
            img_width = float(img_width) - 1
        if float(img_height) % float(2) != 0:
            img_height = float(img_height) - 1
        print(img_width)
        print(img_height)

        for object in objects:
            cname = object.getElementsByTagName("name")[0]
            name = cname.childNodes[0].data
            id_number = categories.get(name)

            bndbox = object.getElementsByTagName("robndbox")[0]
            cx = bndbox.getElementsByTagName("cx")[0]
            cx = cx.childNodes[0].data

            cy = bndbox.getElementsByTagName("cy")[0]
            cy = cy.childNodes[0].data

            w = bndbox.getElementsByTagName("w")[0]
            w = w.childNodes[0].data

            h = bndbox.getElementsByTagName("h")[0]
            h = h.childNodes[0].data

            angle = bndbox.getElementsByTagName("angle")[0]
            angle = angle.childNodes[0].data

            cx = float(cx) * fx
            cy = float(cy) * fy
            w = float(w) * fx
            h = float(h) * fy

            cx = float(cx) / (float(img_width) * fx)
            cy = float(cy) / (float(img_height) * fy)
            w = float(w) / (float(img_width) * fx)
            h = float(h) / (float(img_height) * fy)

            angle = (180 * float(angle)) / 3.14

            temp = id_number + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w) + ' ' + str(h) + ' ' + str(angle) + '\n'
            # print(temp)
            f_w.write(temp)

        f_w.close()

    print("标签缩放完成")


def scale_image():
    # image_path = './inference/scale/input/'
    # image_save_path = './inference/scale/output/'

    image_path = 'C:/Users/MCCC/Desktop/OBBD/hrsc2016/images/train/'
    image_save_path = 'C:/Users/MCCC/Desktop/OBBD/outimg3'

    image_files = os.listdir(image_path)  # 列出所有图像文件

    for image_file in image_files:
        image_filename = os.path.splitext(image_file)[0]  # 分割出图像名
        sufix = os.path.splitext(image_file)[1]  # 分割出后缀
        image_file = os.path.join(image_path, image_file)  # 组合路径
        img = cv2.imread(image_file)
        # width = img.shape[1]
        # height = img.shape[0]

        scale_image = cv2.resize(img, None, fx=fx, fy=fx)

    #cv2.imwrite(os.path.join(image_save_path, "{}_fx_{}_fy_{}.tiff".format(image_filename, fx, fy)), scale_image)
        cv2.imwrite(os.path.join(image_save_path, "{}_fx_{}_fy_{}.bmp".format(image_filename, fx, fy)), scale_image)
#         cv2.imwrite(os.path.join(image_save_path, "{}.tiff".format(image_filename)), scale_image)

    print("缩放图片完成")


if __name__ == '__main__':

    scale_image()   # 缩放图片

    #scale_xml()   # 缩放xml
