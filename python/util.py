import struct
from scipy import sparse as sp
import numpy as np


def read_mat(filename: str) -> sp.csc_matrix:
    """Read sparse matrix from a binary file.
    The file stores data as follows:
    element_count   uint32
    rows            uint32
    columns         uint32
    row_index       uint32 * element_count
    col_index       uint32 * element_count
    data            float64 * element_count
    """
    with open(filename, 'rb') as f:
        raw_data = f.read(4)
        cnt = struct.unpack('I', raw_data)[0]
        raw_data = f.read(4)
        rows = struct.unpack('I', raw_data)[0]
        raw_data = f.read(4)
        cols = struct.unpack('I', raw_data)[0]
        raw_data = f.read(cnt * 4)
        row = np.frombuffer(raw_data, dtype='uint32')
        raw_data = f.read(cnt * 4)
        col = np.frombuffer(raw_data, dtype='uint32')
        raw_data = f.read(cnt * 8)
        data = np.frombuffer(raw_data, dtype='float64')
        return sp.csc_matrix((data, (row, col)), shape=(rows, cols))


def save_mat(filename: str, mat: sp.csc_matrix) -> None:
    """Save csc_matrix to a binary file.
    The file stores data as follows:
    element_count   uint32
    rows            uint32
    columns         uint32
    row_index       uint32 * element_count
    col_index       uint32 * element_count
    data            float64 * element_count
    """
    with open(filename, 'wb') as f:
        cnt = mat.data.size
        raw_data = struct.pack('I', cnt)
        f.write(raw_data)
        hei, wid = mat.shape
        raw_data = struct.pack('I', hei)
        f.write(raw_data)
        raw_data = struct.pack('I', wid)
        f.write(raw_data)
        row, col = mat.nonzero()
        row = row.astype(dtype='uint32')
        col = col.astype(dtype='uint32')
        f.write(bytearray(row.data))
        f.write(bytearray(col.data))
        data = mat.data.astype('float64')
        f.write(bytearray(data.data))


def read_vec(filename: str) -> np.array:
    """Read vector from a binary file.
    The file stores data as follows:
    element_count   uint32
    data            float64 * element_count
    """
    with open(filename, 'rb') as f:
        raw_data = f.read(4)
        cnt = struct.unpack('I', raw_data)[0]
        raw_data = f.read(cnt * 8)
        return np.frombuffer(raw_data, dtype='float64')


def save_vec(filename: str, vec: np.ndarray) -> None:
    """Save vector to a binary file.
    The file stores data as follows:
    element_count   uint32
    data            float64 * element_count
    """
    with open(filename, 'wb') as f:
        vec = vec.astype(dtype='float64')
        cnt = vec.size
        raw_data = struct.pack('I', cnt)
        f.write(raw_data)
        f.write(bytearray(vec.data))
