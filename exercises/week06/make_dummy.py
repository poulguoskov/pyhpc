import numpy as np
arr = np.arange(10).astype('float32')
arr = arr[:, None, None, None]  # (10, 1, 1, 1)
np.save('dummydata.npy', arr)