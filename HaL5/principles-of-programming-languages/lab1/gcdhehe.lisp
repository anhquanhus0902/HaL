(defun gcdhehe(a b)
    (if (= b 0)
        a
        (gcdhehe b (mod a b))
    )
)

(write (gcdhehe (read) (read)))
