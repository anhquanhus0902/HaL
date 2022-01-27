filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p lst = [x | x <- lst, p x]

main = do
	print(filter' (\x -> x > 2) [1,2,3,4,5])
	print(filter' (\x -> x < 6.5) [7.9, 1.2, 12.44, 6.4, 3.33])
