function Ex1w2(fileName1, fileName2)
    imgI = imread(fileName1);
    imgJ = imread(fileName2);
  
    [x, y, z] = size(imgJ);
    imresize(imgI, [x,y]);
    imgdbI = double(imgI)/255;
    
    [x1, y1, z1] = size(imgdbI)
  
    subplot(1, 2, 1), imshow(imgdbI), title(strcat([num2str(x), "x",num2str(y), "x",num2str(z1)]));
    
    subplot(1, 2, 2), imshow(imgJ), title(strcat([num2str(x), "x",num2str(y)]));
endfunction
