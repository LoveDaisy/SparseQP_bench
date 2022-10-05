function write_vec(filename, vec)
% DESCRIPTION
%   It writes a vector array into a binary file.
%   The data stores in file as follows:
%   element_count       uint32
%   data                float64 * element_count
% SYNTAX
%   write_vec(filename, vec)
% INPUT
%   filename:           A string
%   vec:                A vector array

fid = fopen(filename, 'wb');
fwrite(fid, uint32(numel(vec)), 'uint32');
fwrite(fid, vec(:), 'double');
fclose(fid);
end
