;;; none-empty subsets of integer list s that have an even sum
(define (even-subsets s)
  (if (null? s)
      nil
      (append
        ;; don't use first
        (even-subsets (cdr s))

        ;; use first
        (map (lambda (subset) (cons (car s) subset))
             (if (even? (car s))
                 (even-subsets (cdr s))
                 (odd-subsets (cdr s))))

        ;; subset containing only first
        (if (even? (car s))
            (list (list (car s)))
            nil))))

;;; none-empty subsets of integer list s that have an odd sum
(define (odd-subsets s)
  (if (null? s)
      nil
      (append
        ;; don't use first
        (odd-subsets (cdr s))

        ;; use first
        (map (lambda (subset) (cons (car s) subset))
             (if (odd? (car s))
                 (even-subsets (cdr s))
                 (odd-subsets (cdr s))))

        ;; subset containing only first
        (if (odd? (car s))
            (list (list (car s)))
            nil))))
