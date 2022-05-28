function mapping_onto_sphere(filename)
  if ~exist('filename', 'var')
    filename = 're.png';
  endif
  im = imread(filename);
  sphere(100);
  chr = get(gca,'children');
  set(chr,'FaceColor', 'TextureMap' ,'CData' ,flipud(im), 'EdgeColor', 'none');
  axis square
end
