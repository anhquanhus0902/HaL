bmiTell :: Float -> Float -> String
bmiTell height weight
	| bmi < 18.5 = "Gay"
	| bmi < 23 = "Binh thuong"
	| bmi < 25 = "Nguy co beo phi"
	| otherwise = "Beo phi"
	where bmi = weight/height ^2

main = do
	inp1 <- getLine
	inp2 <- getLine
	let height = (read inp1 :: Float)
	let weight = (read inp2 :: Float)
	print(bmiTell bmi)
