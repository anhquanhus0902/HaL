factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

main = do
	inp <- getLine
	let n = (read inp :: Int)
	print(factorial n)
