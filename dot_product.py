import utils
import numpy as np

g22 = np.memmap(filename='g22.npy', mode='r')
g21 = np.memmap(filename='g21.npy', mode='r')

r1 = utils.blockwise_dot(g22,g21)
np.save('final_products/r1', r1)

