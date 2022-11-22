import numpy as np
from collections import Counter
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974., -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431., 29810.], dtype=np.float32)

nans_index = np.isnan(mystery)
c = Counter(np.isnan(mystery))
n_nan = c[True]
mystery_new = mystery
mystery_new[np.isnan(mystery)] = 0
mystery_int = np.int32(mystery)
array = np.sort(mystery)
table = array.reshape((5, 3), order='F')
col = table[:,1]
