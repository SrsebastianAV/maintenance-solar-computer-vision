"""

"""
import os

import cv2


class Gestor_img:
    def __init__(self, img_folder_name):
        self.img_folder_name = os.path.join(img_folder_name)
    def cwd(self):
        """
        Get current working directory CWD
        :return: CWD
        """
        return os.getcwd()
    def img_folder(self):
        """

        :param img_folder_name: Name of the image folder saved on the same os.path.dirname(__file__)
        :return: path with image folder
        """
        return os.path.join(os.path.dirname(__file__), self.img_folder_name)

    def img_path(self):
        """
        List comprehension used to get all the image filenames in a folder (coming of function: img_folder)
        :return: names
        """
        img_path = [os. path.join(self.img_folder(), n) for n in os.listdir(self.img_folder())]
        return img_path
    def plot_imgs(self):
        for p in self.img_path():
            img = cv2.imread(p)
            if img is not None:
                cv2.imshow(f'Image{p}', img)
            else:
                print(f'Could not read image {p}')


