#lang racket

(require "common.rkt")

(define (walker lst [parents null] [acc null] [accs null])
  ;(displayln parents)
  (if (empty? lst)
      (cdr (reverse (cons (reverse acc) accs)))
      (match (string-split (car lst) " ")
        [(list "$" "cd" "..") (walker (cdr lst) (cdr parents) acc accs)]
        [(list "$" "cd" dname) (walker (cdr lst)
                                       (cons dname parents)
                                       (list (apply string-append dname parents))
                                       (cons (reverse acc) accs))]
        [(list "$" "ls") (walker (cdr lst) parents acc accs)]
        [(list "dir" x)  (walker (cdr lst) parents (cons (apply string-append x parents) acc) accs)]
        [(list siz _)  (walker (cdr lst) parents (cons (string->number siz) acc) accs)])))

(define (sizeof dir dirs)
  (apply + (map (λ(x) (if (number? x)
                          x
                          (sizeof x dirs)))
                (cdr (assoc dir dirs)))))

(define input (walker (file->lines "../inputs/7.txt")))
(define dir-sizes (map (curryr sizeof input) (map car input)))

(displayln (apply + (filter (curry >= 100000) dir-sizes)))
(displayln (apply min (filter (λ(x) (>= (- 70000000 (car dir-sizes))
                                        (- 30000000 x)))
                              (cdr dir-sizes))))

