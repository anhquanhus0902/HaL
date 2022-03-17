function bai21(filename)
  imgJ = imread(filename);
  [m, n] = size(imgJ);
  
  for i = 1:m
    for j = 1:n
      imgJ(i,j) = 1 - imgJ(i,j);
    endfor
  endfor
  save alpha.txt imgJ;
  imshow(imgJ);
endfunction