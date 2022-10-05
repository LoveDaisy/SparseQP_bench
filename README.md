# Sparse QP bench

It is a simple benchmark for a large scale sparse quadratic programming (QP) problem.
The QP is formulated as,

$$
\begin{array}{rl}
\min & \frac{1}{2}\mathbf{x}^T \mathbf{Hx} + \mathbf{f}^T \mathbf{x} \\
\text{s.t. } & \mathbf{l} \le \mathbf{x} \le \mathbf{u}
\end{array}
$$

Here I have prepared data for these matrix and vectors, which are stored binary.
And also I have functions to read them in matlab and python. **NOTE**, the data files
are tracked by [GIT LFS](https://git-lfs.github.com/), make sure you have installed it
and pulled the right data files, which are as large as several MBs.

There are two benchmarks. One is to solve the QP, and the other one is to solve an associated linear system of the QP, i.e. $\mathbf{x}=-\mathbf{H}^{-1}\mathbf{f}$.

The QP solver I used in matlab is built-in `quadprog`, and in python is [OSQP](https://osqp.org/docs/index.html), which can be installed easily via `pip3 install osqp`. Please let me know if there is a faster QP solver.

Matlab start script is `matlab/matlab_test.m`, and python is `python/test_qp_solver.py`.
Here is a reference running time (in seconds) on my laptop, Mid 2014 MBP, with 2.5 GHz Quad-Core Intel Core i7 CPU.

| problem | matlab | python (OpenBLAS / MKL) |
---|---|---
| QP | 46.0 | 96.2 / 129.6 |
| Linear system | 0.258 | 1.94 / 1.15 |

In any bench, matlab is much faster than python.

### Data storage layout

The data I put in folder `data` contain all matrix and vectors needed in this bechmark.
If anyone is interested and want to try in other languages, please check this section, and implement your own read/write functions.

For matrix, the data storage layout is as follows,

```
element_count   uint32
rows            uint32
columns         uint32
row_index       uint32 * element_count
col_index       uint32 * element_count
data            float64 * element_count
```

For vector, it is much simpler,

```
element_count   uint32
data            float64 * element_count
```

Of course there are implemented matlab and python version. Please take them as references freely if you want to write your own version.
