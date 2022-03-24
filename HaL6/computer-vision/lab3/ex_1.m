function ex_1()
  
  window = [
    [0,1,1,1,0];
    [1,2,2,2,1];
    [1,1,5,1,1];
    [1,2,2,2,1];
    [0,1,1,1,0];
    ];
  
  originalImg = imread("Image25.jpg");
  grayScaledImg = 0.2989*originalImg(:,:,1) + 0.5870*originalImg(:,:,2) + 0.1140*originalImg(:,:,3);
  grayScaledImg = double(grayScaledImg);
  [m, n] = size(grayScaledImg);
  outputImg = zeros(m, n);
  
  for i=3:m-2
    for j=3:n-2
      v = grayScaledImg(i-2:i+2, j-2:j+2);
      re = sort(reshape(window .* v, 1, []));
      med = median(re);
      outputImg(i, j) = med;
    endfor
  endfor
  
  imshow(uint8(outputImg));
end