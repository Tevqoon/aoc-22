#lang racket

(require srfi/26)

(define (gather lst [accs null] [acc null])
  (match lst
    [(cons #f xs) (gather xs (cons acc accs) null)]
    [(cons x xs) (gather xs accs (cons x acc))]
    [null (cons acc accs)]
    ))

(provide (all-defined-out) cut)
