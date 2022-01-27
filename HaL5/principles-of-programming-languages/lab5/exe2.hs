zip' :: [a] -> [b] -> [(a,b)]
zip' [] [] = []
zip' xs [] = []
zip' [] ys = []
zip' (x:xs) (y:ys) = (x,y) : zip' xs ys

main = do
	print(zip' [1,2,3] [2,3])
