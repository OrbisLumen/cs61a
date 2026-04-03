;;; non-empty subsets of s 
(define (nonempty-subsets s)
  (if (null? s)
    nil
    (let ((rest (nonempty-subsets (cdr s))))
      (append rest
        (map (lambda (t) (cons (car s) t)) rest)
        (list (list (car s)))))))

;;; non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
  (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s)))
