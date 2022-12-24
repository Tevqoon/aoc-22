#lang racket

(require "common.rkt")

(define input (map (λ(line) (match (string-split (string-replace line ":" "") " ")
                              [(list name num) (cons name (string->number num))]
                              [(list name mon1 op mon2)
                               (cons name (list (eval (call-with-input-string op read))
                                                mon1 mon2))]))
                   (file->lines "../inputs/21.txt")))

(define (op-1 op)
  ((λ(x) (if x (cdr x) op)) (assoc op `((,+ . ,-) (,- . ,+) (,* . ,/) (,/ . ,*)))))

(define (solver1 inp [cell "root"])
  (match (cdr (assoc cell inp))
    [(list op a1 a2) (op (solver1 inp a1) (solver1 inp a2))]
    [a a]))

(writeln (solver1 input))

(define (solver2 inp [cell "root"])
  (match (cdr (assoc cell inp))
    [(list op a b)
     (let-values ([(left fl)  (solver2 inp a)]
                  [(right fr) (solver2 inp b)]
                  [(op) (if (equal? cell "root") (λ(x f) f) op)])
       (cond [fl (values left (λ(y) (fl ((op-1 op) y right))))]
             [(and fr (member op (list - /)))
              (values right (λ(y) (fr (op left y))))]
             [fr (values right (λ(y) (fr ((op-1 op) y left))))]
             [else (values (op left right) #f)]))]
    [a (if (equal? cell "humn") (values 'x identity) (values a #f))]))

(writeln (call-with-values (λ() (solver2 input)) (λ(x f) (f 0))))

