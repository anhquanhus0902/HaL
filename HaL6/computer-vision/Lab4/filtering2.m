function filtering2()
  im = imread('./peppers.png');
  grayIm = rgb2gray(im);
  sobelEdge = edge(grayIm, 'sobel');
  prewittEdge = edge(grayIm, 'prewitt');
  robertsEdge = edge(grayIm, 'roberts');
  logEdge = edge(grayIm, 'log');
  cannyEdge = edge(grayIm, 'canny');
  
  subplot(2,3,1);
  imshow(sobelEdge);
  subplot(2,3,2);
  imshow(prewittEdge);
  subplot(2,3,3);
  imshow(robertsEdge);
  subplot(2,3,4);
  imshow(logEdge);
  subplot(2,3,5);
  imshow(cannyEdge);
end  