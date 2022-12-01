#lang racket
(require "common.rkt")

(define input (sort (map (curry apply +)
                         (gather (map string->number
                                      (file->lines "../inputs/1.txt"))))
                    >))

(writeln (car input))
(writeln (apply + (take input 3)))
