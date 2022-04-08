import utils
import numpy as np

g22 = np.memmap(filename='g22.npy', mode='r', shape=(27648,27648))
g21 = np.memmap(filename='g21.npy', mode='r', shape=(27648,27648))

r1 = utils.blockwise_dot(g22,g21)
np.save('final_products/r1', r1)

