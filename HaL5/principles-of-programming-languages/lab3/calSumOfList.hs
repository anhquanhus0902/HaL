calSum :: (Num a) => [a] -> a
calSum [] = 0
calSum (x:xt) = x + calSum xt

main = do
	print(calSum [1, 2, 3, 4, 5])
