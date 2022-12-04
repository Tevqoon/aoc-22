#lang racket

(require "common.rkt")

(define input (map (compose (curry map (compose (curry map string->number)
                                                (curryr string-split "-")))
                            (curryr string-split ","))
                   (file->lines "../inputs/4.txt")))

(define (contained? line)
  (match line
    [(list (list a1 b1) (list a2 b2))
     (or (and (<= a1 a2) (>= b1 b2))
         (and (<= a2 a1) (>= b2 b1)))]))

(define (overlap? line)
  (match line
    [(list (list a1 b1) (list a2 b2))
     (not (or (< b1 a2)
              (< b2 a1)))]))

(writeln (count contained? input))
(writeln (count overlap? input))
