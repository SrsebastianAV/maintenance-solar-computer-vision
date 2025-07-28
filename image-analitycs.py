"""

"""
import pandas as pd
import cv
import tifffile as tiff

dfs = pd.read_csv("C:/Users/SebastiánAguirre/PycharmProjects/SeriesTiempoPrediction/image-processing/thermo/datasets/single-row/metadata.csv")
carpeta_base_s = "C:/Users/SebastiánAguirre/PycharmProjects/SeriesTiempoPrediction/image-processing/thermo/datasets/single-row/thermal images"
dfs["ruta"] = dfs["thermal image name"].apply(lambda x: f"{carpeta_base_s}/{x}")
for i in range(10):
    img = tiff.imread(dfs["ruta"].iloc[i])
    print(img.shape)
    print(img)



