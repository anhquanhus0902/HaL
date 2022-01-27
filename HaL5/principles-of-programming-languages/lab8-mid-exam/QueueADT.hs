module QueueADT (Queue(..), enqueue, dequeue, front) where

data Queue a = Q ([a], [a]) deriving (Show)

enqueue :: a -> Queue a -> Queue a
enqueue x (Q ([], [])) = Q ([x], [])
enqueue x (Q (front, rear)) = Q (front, x:rear)

dequeue :: Queue a -> Queue a
dequeue (Q ([], [])) = error "Queue is empty"
dequeue (Q ((x:xs), rear)) = Q (xs, rear)
dequeue (Q ([], rear)) = dequeue (Q (reverse rear, []))

front :: Queue a -> a
front (Q ([],[])) = error "Queue is empty"
front (Q ((x:xs),(rear))) = x
front (Q ([],rear)) = front (Q ((reverse rear),[]))
