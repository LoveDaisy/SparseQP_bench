import logging
import scipy as sp
import numpy as np
import osqp
import time
from util import read_vec, read_mat

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    data_folder = '../data'

    # Load data
    H = read_mat(f'{data_folder}/H.bin')
    f = read_vec(f'{data_folder}/f.bin')
    lb = read_vec(f'{data_folder}/lb.bin')
    ub = read_vec(f'{data_folder}/ub.bin')

    # Load reference solution
    x0 = read_vec(f'{data_folder}/x.bin')

    num = f.size

    # OSQP solver
    logging.info(f'Solving QP...')

    t0 = time.time()
    solver = osqp.OSQP()
    solver.setup(P=H, q=f, A=sp.sparse.csc_matrix(sp.sparse.identity(num)),
                 l=lb, u=ub, verbose=False, eps_abs=1e-4, eps_rel=1e-4, max_iter=8000)
    sol = solver.solve()
    t1 = time.time()

    logging.info('finish!')
    logging.info(f'  obj: {0.5 * H.dot(sol.x).dot(sol.x) + f.dot(sol.x):.6e}')
    logging.info(f'  violation: {np.sum(sol.x < lb) + np.sum(sol.x > ub)}')
    logging.info(f'  elapse: {t1 - t0:.3f}sec')
    logging.info(f'  abs err: {np.linalg.norm(sol.x - x0)}')
    logging.info(f'  rel err: {np.linalg.norm(sol.x - x0) / np.linalg.norm(x0)}')

    logging.info('Solving linear system...')

    t0 = time.time()
    x_lin = sp.sparse.linalg.spsolve(H, -f)
    t1 = time.time()

    logging.info('finish!')
    logging.info(f'  elapse: {t1 - t0:.3f}sec')
