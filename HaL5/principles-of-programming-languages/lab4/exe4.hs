checkPList :: [Int] -> Bool
checkPList [] = False
checkPList (x:xs)
		| x > 0 && xs == [] = True
checkPList (x:xs)
		| x < 0 = False
		| otherwise = checkPList xs

main = do
	print(checkPList [1,2,3,4,5])
	print(checkPList [44,23,-3,12,3])
	print(checkPList [])
	print(checkPList [1])
