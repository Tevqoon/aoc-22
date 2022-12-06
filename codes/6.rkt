#lang racket

(require "common.rkt")

(define input (string->list (car (file->lines "../inputs/6.txt"))))

(define (check lst len)
  (+ len
     (index-where (apply mapcar list (map (curry drop input)
                                          (range len)))
                  (compose not check-duplicates))))

(writeln (check input 4))
(writeln (check input 14))
