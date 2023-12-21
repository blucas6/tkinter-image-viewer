import os
from PIL import Image, ImageTk
from config import *
from math import floor


def IM_loadImageList(folder):
    IMG_LIST = []
    for file in os.listdir(folder):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".PNG"):
            IMG_LIST.append(os.path.join(file))
    IMG_LIST.sort()
    print(IMG_LIST)
    return IMG_LIST

def IM_viewImage(folder, canvas, img_list, i):
    if img_list:
        path = folder+"/"+img_list[i]
        # print(path, i)
        img = Image.open(path)
        r_img = imageResize(img)
        print("D:", img.width, img.height, "\nNew D:", r_img.width, r_img.height)
        canvas.image = ImageTk.PhotoImage(r_img)
        canvas.create_image(CANVAS_W/2, CANVAS_H/2, image=canvas.image)

def imageResize(img):
    neww = img.width
    newh = img.height
    if img.width > CANVAS_W:
        dw = img.width - CANVAS_W
        r = dw / img.width
        dh = img.height * r
        neww = img.width - dw
        newh = img.height - dh
    if newh > CANVAS_H:
        dh = img.height - CANVAS_H
        r = dh / img.height
        dw = img.width * r
        neww = img.width - dw
        newh = img.height - dh
    return img.resize((floor(neww), floor(newh)))
        

