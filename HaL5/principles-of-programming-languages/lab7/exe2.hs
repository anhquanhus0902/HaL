import BinaryTreeADT

main = do
	let tree = Node (Node (Empty) 3 (Empty)) 5 (Node (Empty) 7 (Empty))
	print(depthTree tree)
	print(preorderTree tree)
	print(inorderTree tree)
	print(postorderTree tree)
