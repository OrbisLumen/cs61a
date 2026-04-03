(define (over-or-under num1 num2)
  (cond ((> num1 num2) (print 1))
    ((= num1 num2) (print 0))
    ((< num1 num2) (print -1))))

(define (make-adder num)
  (lambda (x) (+ x num)))

(define (composed f g)
  (lambda (x) (f (g x))))

(define (repeat f n)
  (define (re g k)
    (cond ((= k 1) g)
      (else (re (composed f g) (- k 1)))))
  (re f n))


(define (max a b)
  (if (> a b)
    a
    b))

(define (min a b)
  (if (> a b)
    b
    a))

(define (gcd a b)
  (if (zero? b) a (gcd (min a b) (modulo (max a b) (min a b)))))
