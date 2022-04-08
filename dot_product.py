import utils
import numpy as np

g22 = np.memmap(filename='g22.npy', mode='r', shape=(27648,27648))
g21 = np.memmap(filename='g21.npy', mode='r', shape=(27648,27648))

r1_mod = utils.blockwise_dot(g22, g21, max_elements=int(2**32))
np.save('final_products/r1d', r1_mod)

r1 = np.dot(g22,g21)
np.save('final_products/r1', r1)

