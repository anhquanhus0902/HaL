function filtering()
  filePath = './peppers.png';
  im = imread(filePath);
  imshow(im);
  grayIm = rgb2gray(im);
  brIm = brighten(double(grayIm), 0.5);
  imshow(brIm);
  cMap = contrast(double(grayIm));
  imshow(grayIm);
  colormap(cMap);
  hisIm = histeq(grayIm);
  imshow(hisIm);
  imshow(imadjust(grayIm));
end