import os
import sys
import blosc
import numpy as np
from time import perf_counter as time

def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()

def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()

def read_numpy(file_name):
    return np.load(f"{file_name}.npy")

def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)

n = int(sys.argv[1])
arr = np.tile(
    np.arange(256, dtype='uint8'),
    (n // 256) * n * n,
).reshape(n, n, n)

t = time()
write_numpy(arr, "test_np")
t_write_np = time() - t

t = time()
write_blosc(arr, "test_bl")
t_write_bl = time() - t

t = time()
read_numpy("test_np")
t_read_np = time() - t

t = time()
read_blosc("test_bl")
t_read_bl = time() - t

print(t_write_np, t_write_bl, t_read_np, t_read_bl)