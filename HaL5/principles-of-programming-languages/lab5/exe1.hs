reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

main = do
	print(reverse' [1, 2, 3, 4])
	print(reverse' [-4, 6, 1, 9])
	print(reverse' ["MIM", "HUS", "PoPL"])
