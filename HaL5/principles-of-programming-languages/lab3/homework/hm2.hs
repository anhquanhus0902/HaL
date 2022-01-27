findIndex :: [Int] -> Int -> Int
findIndex [] target = error "empty list"
findIndex (x:xs) target
		| x == target = 0
		| otherwise = 1 + findIndex xs target

main = do
	print(findIndex [1,7,6,9,5,3] 5)
