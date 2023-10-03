import numpy as np

def uint8(img, max=255, bit_depth=11):
    normalized_img = (max*(img/2048)).astype(np.uint8)
