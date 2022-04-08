import numpy as np

def _block_slices(dim_size, block_size):
    """Generator that yields slice objects for indexing into 
    sequential blocks of an array along a particular axis
    """
    count = 0
    while True:
        yield slice(count, count + block_size, 1)
        count += block_size
        if count > dim_size:
            raise StopIteration

def blockwise_dot(A, B, max_elements=int(2**32), out=None):
    """
    Computes the dot product of two matrices in a block-wise fashion. 
    Only blocks of `A` with a maximum size of `max_elements` will be 
    processed simultaneously.
    """
    
    m,  n = A.shape
    n1, o = B.shape

    if n1 != n:
        raise ValueError('matrices are not aligned')

    if A.flags.f_contiguous:
        # prioritize processing as many columns of A as possible
        max_cols = max(1, max_elements / m)
        max_rows =  max_elements / max_cols

    else:
        # prioritize processing as many rows of A as possible
        max_rows = max(1, max_elements / n)
        max_cols =  max_elements / max_rows

    if out is None:
        out = np.empty((m, o), dtype=np.result_type(A, B))
    elif out.shape != (m, o):
        raise ValueError('output array has incorrect dimensions')

    for mm in _block_slices(m, max_rows):
        out[mm, :] = 0
        for nn in _block_slices(n, max_cols):
            A_block = A[mm, nn].copy()  # copy to force a read
            out[mm, :] += np.dot(A_block, B[nn, :])
            del A_block

    return out