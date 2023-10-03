import numpy as np

def uint8(img, max=255, bit_depth=11):
    max_val = 1 << bit_depth
    normalized_img = (max*(img/max_val)).astype(np.uint8)
    return normalized_img

