module SortedListADT (SortedList(..), insert, delete, member) where
		data SortedList a = SL [a] deriving (Show)

		insert :: (Ord a) => a -> SortedList a -> SortedList a
		insert a (SL lst) = SL(insert' a lst)
		insert' a [] = [a]
		insert' a (x:xs)
				| a <= x 	= a:x:xs
				| otherwise	= x:(insert' a xs)
		
		delete :: (Ord a) => a -> SortedList a -> SortedList a
		delete a (SL lst) = SL(delete' a lst)
		delete' a [] = []
		delete' a (x:xs)
				| a < x		= x:xs
				| a == x	= xs
				| otherwise	= x:(delete' a xs)

		member :: (Ord a) => a -> SortedList a -> Bool
		member a (SL lst) = member' a lst
		member' a [] = False
		member' a (x:xs)
				| a < x		= False
				| a == x	= True
				| otherwise	= member' a xs
