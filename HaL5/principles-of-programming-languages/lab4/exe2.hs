removeU :: [Int] -> [Int]
removeU [] = []
removeU (x:xs)
		| checkContain xs x	= removeU xs
		| otherwise			= x : removeU xs

checkContain :: [Int] -> Int -> Bool
checkContain [] target = False
checkContain (x:xs) target
        | x == target 	= True
		| otherwise		= checkContain xs target

main = do
    print(checkContain [-3, -3, -1, -1, -1, 1, 1, 1, 3, 3, 4, 6, 6, 8, 8, 8, 9, 9] 13)
