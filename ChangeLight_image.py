import random
import os
import cv2

from skimage import exposure

path = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径



def changeLight():
    '''
    adjust_gamma(image, gamma=1, gain=1)函数:
    gamma>1时，输出图像变暗，小于1时，输出图像变亮
    输入：
        img：图像array
    输出：
        img：改变亮度后的图像array
    '''

    image_path = 'C:/Users/MCCC/Desktop/OBBD/hrsc2016/images/train/'
    image_save_path = 'C:/Users/MCCC/Desktop/OBBD/outimg4'

    image_files = os.listdir(image_path)  # 列出所有图像文件
    for image_file in image_files:
        image_filename = os.path.splitext(image_file)[0]  # 分割出图像名
        sufix = os.path.splitext(image_file)[1]  # 分割出后缀
        image_file = os.path.join(image_path, image_file)  # 组合路径，即./JPEGImages_test/000001.jpg
        src = cv2.imread(image_file)

        flag = random.uniform(0.0, 2.0)  ##flag>1为调暗,小于1为调亮
        out_img = exposure.adjust_gamma(src, flag)

        cv2.imwrite(os.path.join(image_save_path, "{}_changelight.bmp".format(image_filename)),out_img)

if __name__ == '__main__':

    changeLight()