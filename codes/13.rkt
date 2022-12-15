#lang racket

(require "common.rkt")

(define input (filter-map (compose (λ(x) (if (equal? eof x) #f x))
                                   (curryr call-with-input-string read)
                                   (curryr string-replace "," " "))
                          (file->lines "../inputs/13.txt")))


(define (check? a b)
  (match (list a b)
    [(list a a) 'no]
    [(list a b) #:when (andmap number? `(,a ,b)) (< a b)]
    [(list '() b) #t]
    [(list a '()) #f]
    [(list (cons a as) (cons b bs)) (let ([checked (check? a b)])
                                      (if (equal? checked 'no)
                                          (check? as bs)
                                          checked))]
    [(list a b) #:when (list? b) (check? (list a) b)]
    [(list a b) #:when (list? a) (check? a (list b))]
    ))

(apply + (map add1 (indexes-where (slice-up input 2) (curry apply check?))))

(let* ([sorted (sort (append input '(((2)) ((6)))) check?)]
       [index2 (+ 1 (index-of sorted '((2))))]
       [index6 (+ 1 (index-of sorted '((6))))])
  (* index2 index6))
