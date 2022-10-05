function write_mat(filename, mat)
% DESCRIPTION
%   It writes a sparse matrix into a binary file.
%   The data stores in file as follows:
%   element_count       uint32
%   rows, cols          uint32
%   row_index           uint32 * element_count
%   col_index           uint32 * element_count
%   data                float64 * element_count
% SYNTAX
%   write_mat(filename, mat)
% INPUT
%   filename:           A string
%   mat:                A sparse matrix

[row, col, data] = find(mat);
fid = fopen(filename, 'wb');
fwrite(fid, uint32([length(data), size(mat, 1), size(mat, 2)]), 'uint32');
fwrite(fid, uint32(row - 1), 'uint32');
fwrite(fid, uint32(col - 1), 'uint32');
fwrite(fid, data, 'double');
fclose(fid);
end
