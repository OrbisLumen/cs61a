(define (square n) (* n n))

(define (pow base exp)
  (define (p res ex)
    (if (odd? ex)
      (if (= ex 1) res (* base (square (p base (/ (- ex 1) 2)))))
      (square (p base (/ ex 2)))))
  (p base exp))

(define (repeatedly-cube n x)
  (if (zero? n)
    x
    (let ((y (repeatedly-cube (- n 1) x)))
      (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))
