#lang racket

(define (gather lst [accs null] [acc null])
  (match lst
    [(cons #f xs) (gather xs (cons acc accs) null)]
    [(cons x xs) (gather xs accs (cons x acc))]
    [null (cons acc accs)]
    ))

(define input (sort (map (curry apply +)
                         (gather (map string->number (file->lines "../inputs/1.txt"))))
                    >))

(writeln (car input))
(writeln (apply + (take input 3)))
