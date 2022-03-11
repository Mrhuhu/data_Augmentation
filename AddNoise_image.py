from skimage.util import random_noise
import os
import cv2


def addNoise():
    '''
    输入：
        img：图像array
    输出：
        img：加入噪声后的图像array,由于输出的像素是在[0,1]之间,所以得乘以255
    '''

    #image_path = 'C:/Users/MCCC/Desktop/OBBD/hrsc2016/images/train/'
    image_path = 'C:/Users/MCCC/Desktop/gf2/'
    image_save_path = 'C:/Users/MCCC/Desktop/outimg6'


    image_files = os.listdir(image_path)  # 列出所有图像文件
    for image_file in image_files:
        image_filename = os.path.splitext(image_file)[0]  # 分割出图像名
        sufix = os.path.splitext(image_file)[1]  # 分割出后缀
        image_file = os.path.join(image_path, image_file)  # 组合路径，即./JPEGImages_test/000001.jpg
        src = cv2.imread(image_file)

        out_img = random_noise(src, mode='gaussian', clip=True) * 255
        print(out_img.shape[2])

        cv2.imwrite(os.path.join(image_save_path, "{}_addnoise.tiff".format(image_filename)),out_img)

if __name__ == '__main__':

    addNoise()