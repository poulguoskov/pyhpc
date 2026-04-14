import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')


def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b] = np.sum(arr[b:e:s], axis=0)


if __name__ == '__main__':
    n_processes = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    chunk = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    # Create shared array
    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    N = len(data)
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run full parallel reduction
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    s = 1
    while s < N:
        pool.map(reduce_step,
                 [(i, min(i + chunk * s, N * s), s, elemshape) for i in range(0, N, chunk * s) if i + s < N],
                 chunksize=1)
        s *= chunk

    print(f"{n_processes},{chunk},{time() - t:.4f}")
    final_image = arr[0] / N
    Image.fromarray(
        (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')