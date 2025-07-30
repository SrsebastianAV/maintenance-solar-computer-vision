"""

"""
#Librerias
import pandas as pd
import cv2
import os
from path import Gestor_img
#
gestor_img_1 = Gestor_img()
print("Carpeta actual:", gestor_img_1.cwd()) #“current working directory” (CWD)
img_folder = gestor_img_1.img_folder("erco_termo")

# path = "C:/Users/SebastiánAguirre/PycharmProjects/SeriesTiempoPrediction/image-processing/erco_termo/imagen (38).jpg"
# print(path)
# img = cv2.imread(path)
# print(img)
# cv2.imshow("", img)
# cv2.waitKey(0)
cv2.destroyAllWindows()
#
# carpeta_base_s = r"C:/Users/SebastiánAguirre/PycharmProjects/SeriesTiempoPrediction/image-processing/erco_termo"
# for i in os.listdir(carpeta_base_s):
#     path = os.path.join(carpeta_base_s, i).replace('\\', '/')
#     print(path)
#     print("Existe?", os.path.exists(path))
#     img = cv2.imread(path)
#     print(img)
#     cv2.imshow('thermo', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# for i in range(10):
#     img = tiff.imread(dfs["ruta"].iloc[i])
#     print(img.shape)
#     print(img)



