module BinaryTreeADT (BinaryTree(..), depthTree, preorderTree, inorderTree, postorderTree) where
		data BinaryTree a = Empty | Node (BinaryTree a) a (BinaryTree a) deriving (Show)

		depthTree :: BinaryTree a -> Int
		depthTree Empty = 0
		depthTree (Node left root right) = 1 + max (depthTree left) (depthTree right)

		preorderTree :: BinaryTree a -> [a]
		preorderTree Empty = []
		preorderTree (Node left root right) = [root] ++ preorderTree left  ++ preorderTree right

		inorderTree :: BinaryTree a -> [a]
		inorderTree Empty = []
		inorderTree (Node left root right) = inorderTree left ++ [root] ++ inorderTree right

		postorderTree :: BinaryTree a -> [a]
		postorderTree Empty = []
		postorderTree (Node left root right) = postorderTree left ++ postorderTree right ++ [root]
