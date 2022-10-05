clear; close all; clc;

% Solve a large scale sparse QP. The Hessian matrix is sparse.
%   min   0.5 * x' * H * x + f' * x
%   s.t.  lb <= x <= ub

% Load data
H = read_mat('../data/H.bin');
f = read_vec('../data/f.bin');
lb = read_vec('../data/lb.bin');
ub = read_vec('../data/ub.bin');

% Load reference solution
x0 = read_vec('../data/x.bin');

% Solve the QP with builtin quadprog function
fprintf('Solving QP...\n');

tic;
x_qp = quadprog(H, f, [], [], [], [], lb, ub);
t_qp = toc;

fprintf('finish!\n');
fprintf('  obj: %.6e\n', 0.5 * x_qp' * H * x_qp + f' * x_qp);
fprintf('  violation: %d\n', sum(x_qp < lb) + sum(x_qp > ub));
fprintf('  elapse: %.2fsec', t_qp);

% Check the solution
assert(norm(x_qp - x0) / norm(x0) < 1e-4);
fprintf('  abs err: %.4e\n', norm(x_qp - x0));
fprintf('  rel err: %.4e\n', norm(x_qp - x0) / norm(x0));

% Solve a linear system
fprintf('Solving linear system...\n');

tic;
x_lin = -H \ f;
t_lin = toc;

fprintf('finish!\n');
fprintf('  elapse: %.3fsec', t_lin);
