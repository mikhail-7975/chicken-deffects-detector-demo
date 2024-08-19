import numpy as np

class ImageFolderReader:
    def __init__(self):
        pass

    def getImage(self):
        return np.random.randint(0, 255, (695, 519, 3), dtype=np.uint8) 