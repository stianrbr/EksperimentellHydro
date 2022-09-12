import numpy as np


def read_binary_file(path, filename):
    file = np.fromfile(path+filename, dtype=float)
    return file