gcdhehe :: Integer -> Integer -> Integer
gcdhehe a b
		| b == 0	= a
		| otherwise	= gcdhehe b (a `mod` b)

main = do
	inp1 <- getLine
	inp2 <- getLine
	let a = (read inp1 :: Integer)
	let b = (read inp2 :: Integer)
	print(gcdhehe a b)
