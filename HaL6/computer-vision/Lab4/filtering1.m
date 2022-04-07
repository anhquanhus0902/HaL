function filtering1()
  im = imread('./peppers.png');
  grayIm = rgb2gray(im);
  dblIm = im2double(grayIm);
  noiseIm = imnoise(dblIm, 'salt & pepper');
  imshow(noiseIm);
  
  hAVG = fspecial('average', 3);
  hGauss = fspecial('gaussian', 9, 1.5);
  
  noiseImAVG = imfilter(noiseIm, hAVG, 'symmetric');
  noiseImMedian = medfilt2(noiseIm);
  noiseImGaussian = imfilter(noiseIm, hGauss, 'symmetric');
  subplot(2,2,1);
  imshow(noiseIm);
  subplot(2,2,2);
  imshow(noiseImAVG);
  subplot(2,2,3);
  imshow(noiseImGaussian);
  subplot(2,2,4);
  imshow(noiseImMedian);
  
  noiseImGuass = imnoise(dblIm, 'gaussian', 0, 1/255);
  noiseImGaussAVG = imfilter(noiseImGuass, hAVG, 'symmetric');
  noiseImGaussMed = medfilt2(noiseImGuass);
  noiseImGaussGaussian = imfilter(noiseImGuass, hGauss, 'symmetric');
  
  subplot(2,2,1);
  imshow(noiseImGuass);
  subplot(2,2,2);
  imshow(noiseImGaussAVG);
  subplot(2,2,3);
  imshow(noiseImGaussGaussian);
  subplot(2,2,4);
  imshow(noiseImGaussMed);
end  