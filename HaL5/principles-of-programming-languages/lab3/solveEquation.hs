solver :: Float -> Float -> Float -> (Float, Float)
solver a b c 
		| d < 0 = error "pt vo nghiem" 
		| otherwise = (x1, x2)
	where	
			x1 = e + sqrt d / (2*a)
			x2 = e - sqrt d / (2*a)	
			d = b*b - 4*a*c
			e = -b / (2*a)

main = do
	inp1 <- getLine
	inp2 <- getLine
	inp3 <- getLine
	let a = (read inp1 :: Float)
	let b = (read inp2 :: Float)
	let c = (read inp3 :: Float)
	print(solver a b c)
