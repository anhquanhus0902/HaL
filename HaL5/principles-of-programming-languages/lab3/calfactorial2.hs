factorial :: Int -> Int
factorial n | n == 0 = 1
			| n /= 0 = n * factorial (n-1)

main = do
	inp <- getLine
	let n = (read inp :: Int)
	print(factorial n)
