data Shape = Circle Float | Rectangle Float Float | Square Float deriving (Eq,Show)

getArea :: Shape -> Float
getArea (Circle r) 		= pi * r * r
getArea (Rectangle h w)	= h * w
getArea (Square l)		= l * l

isRound :: Shape -> Bool
isRound (Circle r)	= True
isRound s			= False

main = do
	let c1 = Circle 4
	let r1 = Rectangle 5.2 1.4
	let s1 = Square 4.4
	print(getArea c1)
	print(getArea r1)
	print(getArea s1)
	print(isRound c1)
	print(isRound r1)
	print(isRound s1)
