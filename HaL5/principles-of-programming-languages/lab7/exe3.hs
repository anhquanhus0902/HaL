import SortedListADT

main = do
	let lst = insert 4 (SL [1, 3, 4, 5])
	print(lst)
	let lst = delete 5 (SL [3,4,5,7,8,12])
	print(lst)
	print(member 5 (SL [1,3,43]))
	print(member 5 (SL [1,2,3,4,5,6,7]))
