getLength :: [Int] -> Int
getLength [] = 0
getLength (_:xt) = 1 + getLength xt

main = do
	print(getLength [3,5,3,1])
