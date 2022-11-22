import numpy as np
def shuffle_seed(array):
    seed = np.random.randint(0, 4294967295)
    np.random.seed(seed)
    new_array = np.random.permutation(array)
    like = (new_array, seed)
    return like

array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))