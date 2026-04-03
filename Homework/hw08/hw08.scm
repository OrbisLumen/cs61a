(define (ascending? s)
  (if (null? s)
    #t
    (if (null? (cdr s))
      #t
      (if (> (car s) (car (cdr s)))
        #f
        (ascending? (cdr s))))))

(define (my-filter pred s)
  (if (null? s) nil
    (if (pred (car s))
      (cons (car s) (my-filter pred (cdr s)))
      (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
  (if (and (null? lst1) (null? lst2))
    nil
    (if (null? lst1)
      lst2
      (if (null? lst2)
        lst1
        (cons (car lst1) (cons (car lst2)
            (interleave (cdr lst1) (cdr lst2))))))))

(define (no-repeats s)
  (if (null? s)
    nil
    (cons (car s) (filter (lambda (x) (not (= x (car s)))) (no-repeats (cdr s))))))
