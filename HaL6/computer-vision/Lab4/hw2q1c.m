function hw2q1c()
  Hx = [[-1,0,1];[-2,0,2];[-1,0,1]];
  Hy = transpose(Hx);
  im = imread('./peppers.png');
  grayIm = rgb2gray(im);
  #res = edge(grayIm, 'sobel');
  [h, w] = size(grayIm);
  
  for i=2:h-2
    for j=2:w-2
      
      E = ceil(sqrt(DX^2 + DY^2));
      grayIm(i,j) = E;
    endfor
  endfor
  
  imshow(res);
end  