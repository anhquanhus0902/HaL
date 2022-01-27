quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = quickSort less ++ [x] ++ quickSort greater
	where
		less = [a | a <- xs, a < x]
		greater = [a | a <- xs, a > x]

main = do
	print(quickSort [6,2,9,4,12])
	print(quickSort [3.6, 2.2, 39.1, 7.8])