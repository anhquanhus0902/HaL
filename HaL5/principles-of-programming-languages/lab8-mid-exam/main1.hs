import ListQueueADT

main = do
    let q = Q [1,2,3,4,5]
    print(q)
    print("front: " ++ show (front q))
    let q' = enqueue 6 q
    let q = q'
    print(q)
    print("front: " ++ show (front q))
    let q' = dequeue q
    let q = q'
    print(q)
    print("front: " ++ show (front q))