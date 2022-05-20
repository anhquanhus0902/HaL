function shadowRemove(filenameI, filenameAlpha)
  r = [1.2 1.0 0.7];
  alpha = load(filenameAlpha);
  [m,n] = size (alpha);
  
  I = ones(m,n);
  
  imgI = imread(filenameI);
  imgI = double(imgI);
  
  for b=1:3
    dbI(:, :, b) = imgI(:, :, b) ./255.0;
  endfor
  
  dbI = imresize(dbI, [m,n]);
  
  for i=1:3
    c_i = dbI(:, :, i);
    rc(:, :, i) = (I*(r(i)+1)) ./ (alpha*r(i)+1) .* c_i;
  endfor
  
  R = rc(:,:,1);
  G = rc(:,:,2);  
  B = rc(:,:,3);
  SF = cat(3, R, G, B);
  
  find_1 = find(SF > 1);
  
  imshow(SF);
end