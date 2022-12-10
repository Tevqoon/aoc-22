#lang racket

(require "common.rkt")

(define input (map (λ(x) (let ([l (string-split x " ")])
                           (list (match (car l)
                                   ["U" '(0  1)]
                                   ["D" '(0 -1)]
                                   ["L" '(-1 0)]
                                   ["R" '(1  0)])
                                 (string->number (cadr l)))))
                   (file->lines "../inputs/9.txt")))

(define (touching? p1 p2)
  (and (<= (abs (- (car  p1) (car  p2))) 1)
       (<= (abs (- (cadr p1) (cadr p2))) 1)))

(define (move1 dir Tposs Hpos)
  (let ([newH (+. Hpos dir)])
    (define (aux Tposs acc prev)
      (if (or (empty? Tposs) (touching? prev (car Tposs)))
          (values (append (reverse acc) Tposs) newH)
          (let ([newT1 (+. (car Tposs)
                           (map (λ(y) (if (zero? y)
                                          y
                                          (/ y (abs y))))
                                (-. prev (car Tposs))))])
            (aux (cdr Tposs) (cons newT1 acc) newT1))))
    (aux Tposs '() newH)))

(define (move movements Tpositions (Hposition '(0 0)) (visited null))
  (match movements
    [(cons (list dir 0) xs)
     (move xs Tpositions Hposition visited)]
    [(cons (list dir n) xs)
     (let-values ([(newTs newH) (move1 dir Tpositions Hposition)])
       (move (cons (list dir (- n 1)) xs) newTs newH (cons (last newTs) visited)))]
    [null (count identity (remove-duplicates visited))]))

(displayln (move input '((0 0))))
(displayln (move input (map (λ(x) '(0 0)) (range 9))))
