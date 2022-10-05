function mat = read_mat(filename)
% DESCRIPTION
%   It reads a sparse matrix from a binary file.
%   The data stores in file as follows:
%   element_count       uint32
%   rows, cols          uint32
%   row_index           uint32 * element_count
%   col_index           uint32 * element_count
%   data                float64 * element_count
% SYNTAX
%   mat = read_mat(filename)
% INPUT
%   filename:           A string
% OUTPUT
%   mat:                A sparse matrix

fid = fopen(filename, 'rb');
cnt = fread(fid, 1, 'uint32');
hei = fread(fid, 1, 'uint32');
wid = fread(fid, 1, 'uint32');

row = fread(fid, cnt, 'uint32');
col = fread(fid, cnt, 'uint32');
data = fread(fid, cnt, 'double');
fclose(fid);

mat = sparse(row + 1, col + 1, data, hei, wid);
end
