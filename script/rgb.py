import os.path
import time

import numpy as np
from PIL import Image


def replace_color(img, src_clr, dst_clr):
    ''' 通过矩阵操作颜色替换程序
    @param	img:	图像矩阵
    @param	src_clr:	需要替换的颜色(r,g,b)
    @param	dst_clr:	目标颜色		(r,g,b)
    @return				替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)

    # 分离通道
    r_img = img_arr[:, :, 0].copy()
    g_img = img_arr[:, :, 1].copy()
    b_img = img_arr[:, :, 2].copy()

    # 编码
    img = r_img * 256 * 256 + g_img * 256 + b_img
    src_color = src_clr[0] * 256 * 256 + src_clr[1] * 256 + src_clr[2]

    # 索引并替换颜色
    r_img[img == src_color] = dst_clr[0]
    g_img[img == src_color] = dst_clr[1]
    b_img[img == src_color] = dst_clr[2]

    # 合并通道
    dst_img = np.array([r_img, g_img, b_img], dtype=np.uint8)
    # 将数据转换为图像数据(h,w,c)
    dst_img = dst_img.transpose((1, 2, 0))

    return dst_img


def replace_color_tran(img):
    ''' 通过遍历颜色替换程序
    @param	img:	图像矩阵
    @return				替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)

    dst_arr = img_arr.copy()
    for i in range(img_arr.shape[1]):
        for j in range(img_arr.shape[0]):
            a = np.asarray(img_arr[j][i], dtype=np.uint8)
            if a[0] < 180 or a[1] < 120 or a[2] < 120:
                b = np.asarray((222, 25, 38), dtype=np.uint8)
                # print(img_arr[j][i], "->", b)
                dst_arr[j][i] = b

    return np.asarray(dst_arr, dtype=np.uint8)


if __name__ == '__main__':
    start = time.time()
    img = Image.open('pingfan.jpg').convert('RGB')
    dst_img = replace_color_tran(img)
    res_img = Image.fromarray(dst_img)
    if os.path.exists("pf-red.jpg"): os.remove("pf-red.jpg")
    res_img.save('pf-red.jpg')
    print(time.time()-start)
