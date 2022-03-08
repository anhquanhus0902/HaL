function ChromaKeying(fileName, fileName2)
  
  imgI = imread(fileName);
  [m, n, o] = size (imgI);
  data = load(fileName2);
  
  K1 = zeros(m, n);
  K2 = zeros(m, n);
  K3 = zeros(m, n);
  K = zeros(m, n, 3);
  
  for j = 1:n
    count = 1;
    for i = (j-1)*m+1:j*m
      if data(i, 4) == 1
        K1(count, j) = 0;
        K2(count, j) = 0;
        K3(count, j) = 0;
      else
        K1(count, j) = data(i, 1);
        K2(count, j) = data(i, 2);
        K3(count, j) = data(i, 3);
      endif
      count += 1;
    endfor
  endfor
  K(:, :, 1) = K1;
  K(:, :, 2) = K2;
  K(:, :, 3) = K3;
  imshow(uint8(K));
endfunction