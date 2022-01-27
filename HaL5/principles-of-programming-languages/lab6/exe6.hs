nPrimes :: Int -> [Int]
nPrimes n = [x | x <- [1..n-1], isPrime x]

isPrime x = if x > 1 then null [i | i <- [2..x-1], x `mod` i == 0] else False

main = do
	print(nPrimes 0)
	print(nPrimes 1)
	print(nPrimes 40)
	print(nPrimes 133)
