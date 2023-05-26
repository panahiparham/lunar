import numpy as np
from PIL import Image
import cv2


print('Lunar topography!')


IMG_PATH = 'data/SLDEM2015_DATA_QUALITY_FLOAT.IMG'
META_PATH = 'data/SLDEM2015_DATA_QUALITY_FLOAT.LBL'



def load_data():
    """
    Load the data from the IMG file.
    """
    
    data = np.fromfile(IMG_PATH, dtype=np.byte)
    return data



def load_meta():
    """
    Load the metadata from the LBL file.
    """
    with open(META_PATH, 'r') as f:
        meta = f.read()
    return meta


def main():
    """
    Main function.
    """
    data = load_data()
    meta = load_meta()

    print(meta)


if __name__ == '__main__':
    main()