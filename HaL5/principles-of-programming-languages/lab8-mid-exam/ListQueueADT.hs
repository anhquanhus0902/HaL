module ListQueueADT (Queue(..), enqueue, dequeue, front) where
data Queue a = Q [a] deriving (Show)

enqueue :: a -> Queue a -> Queue a
enqueue x (Q xs) = Q (xs ++ [x])

dequeue :: Queue a -> Queue a
dequeue (Q (x:xs)) = Q xs
dequeue (Q []) = error "empty queue"

front :: Queue a -> a
front (Q (x:xs)) = x
front (Q []) = error "empty queue"