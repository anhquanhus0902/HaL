negAll :: [Int] -> [Int]
negAll [] = []
negAll (x:xs) = -x : negAll xs

main = do
	print(negAll [1, -7, 9, -6, 7])
