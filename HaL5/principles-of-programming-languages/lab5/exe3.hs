elem' :: (Eq a) => a -> [a] -> Bool
elem' target [] = False
elem' target (x:xs)
		| x == target	= True
		| otherwise		= elem' target xs

main = do	
	print(elem' 4 	[17, 12, 4, 9, 24])
	print(elem' 12 [17, 12, 4, 9, 24])
	print(elem' 33 [17, 12, 4, 9, 24])
	print(elem' "mim" ["hello", "world", "mim", "hus"])
	print(elem' "haha" ["hello", "world", "mim", "hus"])
