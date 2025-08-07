"""

"""
#Librerias
import pandas as pd
import cv2
import os
from path import Gestor_img
#
# gestor_img_1 = Gestor_img("erco_termo")
# print("Carpeta actual:", gestor_img_1.cwd()) #“current working directory” (CWD)
# img_folder = gestor_img_1.img_folder()
# paths = gestor_img_1.img_path()
# print(paths)
# gestor_img_1.plot_imgs()

# path = r"C:\Users\SebastiánAguirre\PycharmProjects\SeriesTiempoPrediction\image-processing"
path = 'erco_termo'
img_names = [n for n in os.listdir(path) if n.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))] #n.lower() -> used to transform string in minusculas
print(img_names)

img = cv2.imread(img_names[14])
print(img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert the bgr to rgb format
b, g, r = cv2.split(img_rgb)
cv2.imshow("vb", img_rgb)
cv2.imshow("b", b)
cv2.imshow("c", g)
cv2.imshow("d", r)
cv2.waitKey(0)
cv2.destroyAllWindows()




