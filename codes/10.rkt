#lang racket

(require "common.rkt")

(define input (map (λ(l) (match (string-split l " ")
                           [(list x) (list x)]
                           [(list x n) (list x (string->number n))]))
                   (file->lines "../inputs/10.txt")))

(define (step instrs (reg 1) (bookmarks null) (stepnum 1))
  (match instrs
    [(cons (list "noop") xs)
     (step xs
           reg
           (map (λ(x) (if (equal? x stepnum)
                          (list x reg)
                          x))
                bookmarks)
           (+ 1 stepnum))]
    [(cons (list "addx" n) xs)
     (step xs
           (+ reg n)
           (map (λ(x) (if (or (equal? x stepnum)
                              (equal? x (+ stepnum 1)))
                          (list x reg)
                          x))
                bookmarks)
           (+ 2 stepnum)
           )]
    [null bookmarks]))

(apply + (map (curry apply *) (step input 1 '(20 60 100 140 180 220) 1)))
(map (compose displayln
              (curry apply string-append))
     (slice-up (map (λ(x) (match x
                            [(list x pos)
                             (if (<= (abs (- (modulo x 40) pos)) 1)
                                 "█"
                                 " "
                                 )]))
                    (step input 1 (range 240) 0))
               40)) 
