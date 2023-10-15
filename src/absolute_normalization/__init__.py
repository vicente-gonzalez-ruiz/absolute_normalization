import numpy as np

def uint8(img, max=255, bit_depth=11):
    max_val = 1 << bit_depth
    normalized_img = (max*(img/max_val)).astype(np.uint8)
    info = "\"uint8\"\t"
    info += f"max={max}\t"
    info += f"bit_depth={bit_depth}\t"
    info += f"max_val={max_val}"
    return normalized_img, info

