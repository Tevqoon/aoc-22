#lang racket

(require "common.rkt")

(define (process-op op)
  (match (string-split op " ")
    [(list _ _ _ _ _ op "old")
     (λ(x) ((eval (call-with-input-string op read)) x x))]
    [(list _ _ _ _ _ op n)
     (λ(x) ((eval (call-with-input-string op read)) x (string->number n)))]
    ))

(define (get-numbers str)
  (filter-map string->number (string-split str " ")))

(define (process monkey)
  (match monkey
    [(list _ s op te tu f)
     (list (get-numbers (string-replace s "," " ")) ; Monkey starting items
           (process-op op)
           (λ(x)
             (if (= 0 (modulo x (car (get-numbers te))))
                 (car (get-numbers tu))
                 (car (get-numbers f)))))]
    ))

(define (transform-value holdings transforms ifs index (divide? #t))
  (let*-values
      ([(monkey) (list-ref holdings index)]
       [(val) (car monkey)]
       [(new-val) (if divide?
                      (floor (/ ((list-ref transforms index) val) 3))
                      (modulo ((list-ref transforms index) val)
                              (* 19 13 5 7 17 2 3 11)
                              ; LCM vseh testov, ni se mi dalo spreminjati oblike inputa
                              )
                      ;;((list-ref transforms index) val)
                      )]
       [(hd tl) (split-at holdings index)]
       [(new-index) ((list-ref ifs index) new-val)]
       [(new-lst) (append hd (list (cdr monkey)) (cdr tl))]
       [(newhd newtl) (split-at new-lst new-index)]
       [(new-newtl) (append (car newtl) (list new-val))]
       [(new-newlst) (append newhd (list new-newtl) (cdr newtl))])
    new-newlst
    ))

(define (step holding transforms ifs (index 0)
              (monkey-counts (map (curry count identity) holding))
              (divide? #t))
  (define (aux holdings aux-monkey-counts)
    (if (empty? (list-ref holdings index))
        (step holdings transforms ifs (+ 1 index) aux-monkey-counts divide?)
        (begin (aux (transform-value holdings transforms ifs index divide?)
                    (+. aux-monkey-counts
                        (map (λ(x) (if (= x index) 1 0))
                             (range (length holding)))))))
    )
  (if (= (length holding) index)
      (values holding monkey-counts)
      (aux holding monkey-counts))
  )

(define (stepper holding transforms ifs steps (divide? #t)
                 (monkey-counts (map (λ(x) 0) (range (length holding)))))
  (if (= 0 steps)
      monkey-counts
      (let*-values ([(new-monkeys new-monkey-counts) (step holding transforms ifs 0 monkey-counts divide?)])
        (stepper new-monkeys transforms ifs (- steps 1) divide? new-monkey-counts))
    )
  )

(define input (transpose (map process (gather (file->lines "../inputs/11.txt") ""))))

(apply * (take (sort (stepper (car input) (cadr input) (caddr input) 20) >=) 2))
;; Takes some time, would be faster without all the list copying in a non-racket language
;; What can you do
(apply * (take (sort (stepper (car input) (cadr input) (caddr input) 10000 #f) >=) 2))


