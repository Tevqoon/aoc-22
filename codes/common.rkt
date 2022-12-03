#lang racket

(require srfi/26)

(define (gather lst [accs null] [acc null])
  "Gathers up the elements of a list into a list of lists, by #f used as marker"
  (match lst
    [(cons #f xs) (gather xs (cons (reverse acc) accs) null)]
    [(cons x xs) (gather xs accs (cons x acc))]
    [null (reverse (cons (reverse acc) accs))]
    ))

(define (slice-up lst n [acc null])
  "Slices up a list into sublists length n. Excess elements dropped."
  (if (< (length lst) n)
      (reverse acc)
      (call-with-values (λ () (split-at lst n))
                        (λ (hd tl) (slice-up tl n (cons hd acc))))))

(provide (all-defined-out) cut)
