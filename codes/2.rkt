#lang racket

(require "common.rkt")

(define (play hand)
  (match hand
    [(cons x x) (+ 3 x)]
    [(cons x y) #:when (= 1 (modulo (- y x)
                                    3))
                (+ 6 y)]
    [(cons x y) y]
    ))

(define (get-hand hand)
  (match hand
    [(cons 1 1) (cons 1 3)]
    [(cons x 1) (cons x (- x 1))] 
    [(cons x 2) (cons x x)] 
    [(cons 3 3) (cons 3 1)]
    [(cons x 3) (cons x (+ x 1))] 
    ))

(define input (map (λ (x)
                     (cons (- (char->integer (string-ref x 0))
                              64)
                           (- (char->integer (string-ref x 2))
                              64
                              23)))
                   (file->lines "../inputs/2.txt")))

(writeln (apply + (map play
                       input)))
(writeln (apply + (map (compose play get-hand)
                       input)))
