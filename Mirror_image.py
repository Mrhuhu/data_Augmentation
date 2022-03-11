import cv2
import math
import os
import xml.dom.minidom
import numpy as np

path = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径

indir = path + "/inference/mirror/xml"  # 输入的xml标签
outdir = path + "/inference/mirror/txt"   # 输出的txt标签


def Vertically_xml(file, Object, categories, img_width, img_height):
    file_save = file.split('.')[0] + '_Vertically' + '.txt'
    file_txt = os.path.join(outdir, file_save)
    f_w = open(file_txt, 'w')
    for object in Object:
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
        angle1 = math.degrees(float(angle))

        cx = float(cx)
        cy = float(img_height) - float(cy)
        angle = math.radians(180 - angle1)

        cx = float(cx) / float(img_width)
        cy = float(cy) / float(img_height)
        w = float(w) / float(img_width)
        h = float(h) / float(img_height)

        angle = (180 * float(angle)) / 3.14

        temp = id_number + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w) + ' ' + str(h) + ' ' + str(angle) + '\n'
        # print(temp)
        f_w.write(temp)

    f_w.close()


def Horizontal_xml(file, Object, categories, img_width, img_height):
    file_save = file.split('.')[0] + '_Horizontal' + '.txt'
    file_txt = os.path.join(outdir, file_save)
    f_w = open(file_txt, 'w')
    for object in Object:
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
        angle1 = math.degrees(float(angle))

        cx = float(img_width) - float(cx)
        cy = float(cy)
        angle = math.radians(180 - angle1)

        cx = float(cx) / float(img_width)
        cy = float(cy) / float(img_height)
        w = float(w) / float(img_width)
        h = float(h) / float(img_height)

        angle = (180 * float(angle)) / 3.14

        temp = id_number + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w) + ' ' + str(h) + ' ' + str(angle) + '\n'
        # print(temp)
        f_w.write(temp)

    f_w.close()


def Cross_xml(file, Object, categories, img_width, img_height):
    file_save = file.split('.')[0] + '_Cross' + '.txt'
    file_txt = os.path.join(outdir, file_save)
    f_w = open(file_txt, 'w')
    for object in Object:
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
        angle1 = math.degrees(float(angle))

        cx = float(img_width) - float(cx)
        cy = float(img_height) - float(cy)
        angle = math.radians(180 - angle1)
        angle2 = math.degrees(angle)
        angle = math.radians(180 - angle2)

        cx = float(cx) / float(img_width)
        cy = float(cy) / float(img_height)
        w = float(w) / float(img_width)
        h = float(h) / float(img_height)

        angle = (180 * float(angle)) / 3.14

        temp = id_number + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w) + ' ' + str(h) + ' ' + str(angle) + '\n'
        # print(temp)
        f_w.write(temp)

    f_w.close()


def Mirror_xml():
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
        # file_save = file.split('.')[0] + '_Vertically' + '.txt'
        # file_txt = os.path.join(outdir, file_save)
        # f_w = open(file_txt, 'w')
        DOMTree = xml.dom.minidom.parse(file)
        annotation = DOMTree.documentElement

        objects = annotation.getElementsByTagName("object")
        img_width = annotation.getElementsByTagName('width')[0].firstChild.nodeValue
        img_height = annotation.getElementsByTagName('height')[0].firstChild.nodeValue
        print(img_width)
        print(img_height)
        img_depth = annotation.getElementsByTagName('depth')[0].firstChild.nodeValue

        Vertically_xml(file, objects, categories, img_width, img_height)
        print("垂直镜像XML标签完成")

        Horizontal_xml(file, objects, categories, img_width, img_height)
        print("水平镜像XML标签完成")

        Cross_xml(file, objects, categories, img_width, img_height)
        print("对角镜像XML标签完成")

    print("镜像XML标签完成")


def Mirror_image():
    #image_path = './inference/mirror/input'
    #image_save_path = './inference/mirror/output'

    image_path = 'C:/Users/MCCC/Desktop/OBBD/hrsc2016/images/train/'
    image_save_path = 'C:/Users/MCCC/Desktop/OBBD/outimg'

    image_files = os.listdir(image_path)  # 列出所有图像文件
    for image_file in image_files:
        image_filename = os.path.splitext(image_file)[0]  # 分割出图像名
        sufix = os.path.splitext(image_file)[1]  # 分割出后缀
        image_file = os.path.join(image_path, image_file)  # 组合路径，即./JPEGImages_test/000001.jpg
        src = cv2.imread(image_file)

        horizontal = cv2.flip(src, 1, dst=None)  # 水平镜像，
        vertical = cv2.flip(src, 0, dst=None)  # 垂直镜像
        cross = cv2.flip(src, -1, dst=None)  # 对角镜像

        #cv2.imwrite(os.path.join(image_save_path, "{}_Horizontal.tiff".format(image_filename)), horizontal)
        cv2.imwrite(os.path.join(image_save_path, "{}_Horizontal.bmp".format(image_filename)), horizontal)
        print("水平镜像完成")
        #cv2.imwrite(os.path.join(image_save_path, "{}_Vertically.tiff".format(image_filename)), vertical)
        cv2.imwrite(os.path.join(image_save_path, "{}_Vertically.bmp".format(image_filename)), vertical)
        print("垂直镜像完成")
        #cv2.imwrite(os.path.join(image_save_path, "{}_Cross.tiff".format(image_filename)), cross)
        cv2.imwrite(os.path.join(image_save_path, "{}_Cross.bmp".format(image_filename)), cross)
        print("对角镜像完成")

    print("镜像完成")


if __name__ == '__main__':

    Mirror_image()

    #Mirror_xml()