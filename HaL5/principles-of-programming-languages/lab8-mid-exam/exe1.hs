import QueueADT

main = do
	let q = (Q ([1, 2], [6, 5, 4, 3]))
	print(q)
	print("front: " ++ show(front q))
	let q' = enqueue 7 q
	let q = q'
	print(q)
	print("front: " ++ show(front q))
	let q'' = dequeue q
	let q = q''
	print(q)
	print("front: " ++ show(front q))
	let q'' = dequeue q
	let q = q''
	print(q)
	print("front: " ++ show(front q))
	let q'' = dequeue q
	let q = q''
	print(q)
	print("front: " ++ show(front q))
