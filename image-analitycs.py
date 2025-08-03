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

path = r"C:/Users/SebastiánAguirre/PycharmProjects/SeriesTiempoPrediction/image-processing/erco_termo/imagen.jpg"
print(path)
img = cv2.imread(path)
print(img)
cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




