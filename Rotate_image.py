from math import *
import cv2
import os
import math
import xml.dom.minidom

path = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径
Rotate_angle = 140  # 角度
Rotate90 = math.radians(90)   # 将90度转换为弧度
if 0 <= Rotate_angle <= 90:
    Rotate_angle1 = math.radians(Rotate_angle)    # 角度转换为弧度
elif 90 < Rotate_angle <= 180:
    Rotate_angle1 = math.radians(Rotate_angle - 90)  # 角度转换为弧度
elif 180 < Rotate_angle <= 270:
    Rotate_angle1 = math.radians(Rotate_angle - 90 - 90)
elif 270 < Rotate_angle <= 360:
    Rotate_angle1 = math.radians(Rotate_angle - 180 - 90)
else:
    print("角度输入错误！")


def get_rotate_xml():
    indir = path + '/inference/rotate/xml'  # xml目录
    outdir = path + '/inference/rotate/txt'  # txt目录
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
        file_save = file.split('.')[0] + '_rotation_' + str(Rotate_angle) + '.txt'
        print(file_save)
        # file_txt = os.path.join(outdir, file_save)"{}_rotation_{}.tiff".format(image_filename, degree))
        file_txt = os.path.join(outdir, file_save)
        print(file_txt)
        f_w = open(file_txt, 'w')
        # actual parsing
        DOMTree = xml.dom.minidom.parse(file)
        annotation = DOMTree.documentElement

        objects = annotation.getElementsByTagName("object")
        img_width = annotation.getElementsByTagName('width')[0].firstChild.nodeValue
        img_height = annotation.getElementsByTagName('height')[0].firstChild.nodeValue
        print(img_width)
        print(img_height)
        img_depth = annotation.getElementsByTagName('depth')[0].firstChild.nodeValue

        if 0 <= Rotate_angle <= 90:
            rotate_img_width = float(img_height) * math.cos(Rotate90 - Rotate_angle1) + float(img_width) * math.cos(
                Rotate_angle1)
            rotate_img_height = float(img_height) * math.sin(Rotate90 - Rotate_angle1) + float(img_width) * math.sin(
                Rotate_angle1)
            # print(int(rotate_img_width))
            # print(int(rotate_img_height))
        elif 90 < Rotate_angle <= 180:
            rotate_img_width = float(img_width) * math.cos(Rotate90 - Rotate_angle1) + float(img_height) * math.cos(
                Rotate_angle1)
            rotate_img_height = float(img_width) * math.sin(Rotate90 - Rotate_angle1) + float(img_height) * math.sin(
                Rotate_angle1)
            # print(int(rotate_img_width))
            # print(int(rotate_img_height))
        elif 180 < Rotate_angle <= 270:
            rotate_img_width = float(img_height) * math.cos(Rotate90 - Rotate_angle1) + float(img_width) * math.cos(
                Rotate_angle1)
            rotate_img_height = float(img_height) * math.sin(Rotate90 - Rotate_angle1) + float(img_width) * math.sin(
                Rotate_angle1)
            # print(int(rotate_img_width))
            # print(int(rotate_img_height))
        elif 270 < Rotate_angle <= 360:
            rotate_img_width = float(img_width) * math.cos(Rotate90 - Rotate_angle1) + float(img_height) * math.cos(
                Rotate_angle1)
            rotate_img_height = float(img_width) * math.sin(Rotate90 - Rotate_angle1) + float(img_height) * math.sin(
                Rotate_angle1)
            # print(int(rotate_img_width))
            # print(int(rotate_img_height))

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

            if 0 <= Rotate_angle <= 90:
                cx2 = math.pow(float(cx), 2)
                cy2 = math.pow(float(cy), 2)
                c = math.sqrt(cx2 + cy2)
                sin_angle = float(cx) / float(c)
                Sin_angle = math.asin(sin_angle)
                B = Rotate90 - Sin_angle - Rotate_angle1
                cx = math.cos(B) * c
                cy = math.sin(B) * c + float(img_width) * math.sin(Rotate_angle1)
                angle = float(angle) - float(Rotate_angle1)

            elif 90 < Rotate_angle <= 180:
                cx2 = math.pow(float(cx), 2)
                cy2 = math.pow(float(cy), 2)
                c = math.sqrt(cx2 + cy2)
                sin_angle = float(cx) / float(c)
                Sin_angle = math.asin(sin_angle)
                B = Sin_angle + Rotate_angle1
                cx = float(img_width) * math.sin(Rotate_angle1) + math.cos(B) * c
                cy = float(img_height) * math.sin(Rotate_angle1) + float(img_width) * math.cos(
                    Rotate_angle1) - math.sin(B) * c
                angle = float(angle) - float(Rotate90) - float(Rotate_angle1)

            elif 180 < Rotate_angle <= 270:
                # h1 = float(cx) / math.tan(Rotate_angle1)
                # h2 = float(img_height) - h1 - float(cy)
                # cx = float(img_width) * math.cos(Rotate_angle1) + math.sin(Rotate_angle1) * h2
                # cy = h1 / math.cos(Rotate_angle1) + h2 * math.cos(Rotate_angle1)
                cx2 = math.pow(float(cx), 2)
                cy2 = math.pow(float(cy), 2)
                c = math.sqrt(cx2 + cy2)
                sin_angle = float(cy) / float(c)
                Sin_angle = math.asin(sin_angle)
                B = Sin_angle - Rotate_angle1
                cx = float(img_width) * math.cos(Rotate_angle1) + float(img_height) * math.sin(
                    Rotate_angle1) - math.cos(B) * c
                cy = float(img_height) * math.cos(Rotate_angle1) - math.sin(B) * c
                angle = float(angle) - 2 * float(Rotate90) - float(Rotate_angle1)

            elif 270 < Rotate_angle <= 360:
                cx2 = math.pow(float(cx), 2)
                cy2 = math.pow(float(cy), 2)
                c = math.sqrt(cx2 + cy2)
                sin_angle = float(cx) / float(c)
                Sin_angle = math.asin(sin_angle)
                B = Rotate90 - Sin_angle - Rotate_angle1
                cx = float(img_height) * math.cos(Rotate_angle1) - c * math.sin(B)
                cy = c * math.cos(B)
                angle = float(angle) - 3 * float(Rotate90) - float(Rotate_angle1)

            cx = float(cx) / float(rotate_img_width)
            cy = float(cy) / float(rotate_img_height)
            w = float(w) / float(rotate_img_width)
            h = float(h) / float(rotate_img_height)

            angle = (180 * float(angle)) / 3.14

            temp = id_number + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w) + ' ' + str(h) + ' ' + str(angle) + '\n'
            print(temp)
            f_w.write(temp)

        f_w.close()


def createListDim(num):
    n = 0
    res = []
    for i in range(num):
        n += 10
        res.append(n)
    return res      # 返回列表格式


#  得到旋转图片
def get_rotate_image():
    # image_path = './inference/rotate/input/'
    # image_save_path = './inference/rotate/output/'
    image_path = 'C:/Users/MCCC/Desktop/OBBD/hrsc2016/images/train/'
    image_save_path = 'C:/Users/MCCC/Desktop/OBBD/outimg2'

    image_files = os.listdir(image_path)  # 列出所有图像文件
    # list = createListDim(35)
    # Rotate_angle = 10
    print(list)
    for image_file in image_files:
        image_filename = os.path.splitext(image_file)[0]  # 分割出图像名
        sufix = os.path.splitext(image_file)[1]  # 分割出后缀
        image_file = os.path.join(image_path, image_file)  # 组合路径，即./JPEGImages_test/000001.jpg
        img = cv2.imread(image_file)
        height, width = img.shape[:2]
        # 旋转后的尺寸
        heightNew = int(width * fabs(sin(radians(Rotate_angle))) + height * fabs(cos(radians(Rotate_angle))))  # 这个公式参考之前内容
        widthNew = int(height * fabs(sin(radians(Rotate_angle))) + width * fabs(cos(radians(Rotate_angle))))
        matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), Rotate_angle, 1)
        matRotation[0, 2] += (widthNew - width) / 2  # 因为旋转之后,坐标系原点是新图像的左上角,所以需要根据原图做转化
        matRotation[1, 2] += (heightNew - height) / 2
        imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(0, 0, 0))
        cv2.imwrite(os.path.join(image_save_path, "{}_rotation_{}.tiff".format(image_filename, Rotate_angle)), imgRotation)
        # for degree in list:
        #     # 旋转后的尺寸
        #     heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))  # 这个公式参考之前内容
        #     widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
        #     matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
        #     matRotation[0, 2] += (widthNew - width) / 2  # 因为旋转之后,坐标系原点是新图像的左上角,所以需要根据原图做转化
        #     matRotation[1, 2] += (heightNew - height) / 2
        #     imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(0, 0, 0))
#  cv2.imwrite(os.path.join(image_save_path, "{}_rotation_{}.tiff".format(image_filename, degree)), imgRotation)
    print('旋转成功')


if __name__ == '__main__':

    get_rotate_image()   # 得到旋转图片

    #get_rotate_xml()   # 得到旋转后的xml

