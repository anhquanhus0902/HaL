data Signal = Red | Yellow | Green deriving (Eq)

stopWhen:: Signal -> Bool
stopWhen c	| c==Red	= True
			| otherwise	= False

main = do
	print(stopWhen Red)
	print(stopWhen Yellow)
	print(stopWhen Green)
