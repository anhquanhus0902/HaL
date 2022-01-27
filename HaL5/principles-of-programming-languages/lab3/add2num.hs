add :: Int -> Int -> Int
add a b = a + b

main = do
	inp1 <- getLine
	inp2 <- getLine
	let a = (read inp1 :: Int)
	let b = (read inp2 :: Int)
	print(add a b)
