function vec = read_vec(filename)
% DESCRIPTION
%   It reads a vector array from a binary file.
%   The data stores in file as follows:
%   element_count       uint32
%   data                float64 * element_count
% SYNTAX
%   vec = read_vec(filename)
% INPUT
%   filename:           A string
% OUTPUT
%   vec:                A vector array

fid = fopen(filename, 'rb');
cnt = fread(fid, 1, 'uint32');
vec = fread(fid, cnt, 'double');
vec = vec(:);
fclose(fid);
end
