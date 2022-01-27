mergeTwoList :: [Int] -> [Int] -> [Int]
mergeTwoList [] [] = []
mergeTwoList xs [] = xs
mergeTwoList [] ys = ys
mergeTwoList (x:xs) (y:ys) = if x < y
								then x : (mergeTwoList xs (y:ys))
								else y : (mergeTwoList (x:xs) ys)
main = do
	print(mergeTwoList [1,1,3, 6, 9] [2, 4, 7, 8, 12])
