#lang racket

(require "common.rkt")

(define (charint->priority charint)
  (if (<= charint 90)
      (- charint 38)
      (- charint 96)))

(define input (map (compose (curry map (compose charint->priority char->integer))
                            string->list)
                   (file->lines "../inputs/3.txt")))

(writeln (apply + (map (compose car
                                (curry apply set-intersect)
                                (λ (l) (call-with-values
                                        (λ () (split-at l (/ (length l) 2)))
                                        list))) 
                       input)))

(writeln (apply + (map (compose car
                                (curry apply set-intersect))
                       (slice-up input 3))))

