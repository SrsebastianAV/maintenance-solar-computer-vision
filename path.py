"""

"""
import os


class Gestor_img:
    def __init__(self):
        pass
    def cwd(self):
        """
        Get current working directory CWD
        :return: CWD
        """
        return os.getcwd()
    def img_folder(self, img_folder_name):
        """

        :param img_folder_name: Name of the image folder saved on the same os.path.dirname(__file__)
        :return: path with image folder
        """
        return os.path.join(os.path.dirname(__file__), img_folder_name)

    def img_names(self):
        pass
