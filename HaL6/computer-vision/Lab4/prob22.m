function prob22()
  filePath = 'pic_1151313471_10.jpg';
  im = imread(filePath);
  hsvIm = rgb2hsv(im);
  
  rIm = im(:,:,1);
  gIm = im(:,:,2);
  bIm = im(:,:,3);
  
  hIm = hsvIm(:,:,1);
  sIm = hsvIm(:,:,2);
  vIm = hsvIm(:,:,3);
  
  subplot(2,3,1);
  imshow(rIm);
  subplot(2,3,2);
  imshow(gIm);
  subplot(2,3,3);
  imshow(bIm);
  subplot(2,3,4);
  imshow(hIm);
  subplot(2,3,5);
  imshow(sIm);
  subplot(2,3,6);
  imshow(vIm);
end