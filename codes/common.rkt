#lang racket

(require srfi/26)

(define (gather lst [marker #f] [accs null] [acc null])
  "Gathers up the elements of a list into a list of lists, by #f used as marker"
  (match lst
    [(cons x xs) #:when (equal? x marker) (gather xs marker (cons (reverse acc) accs) null)]
    [(cons x xs) (gather xs marker accs (cons x acc))]
    [null (reverse (cons (reverse acc) accs))]
    ))

(define (slice-up lst n [acc null])
  "Slices up a list into sublists length n. Excess elements dropped."
  (if (< (length lst) n)
      (reverse acc)
      (call-with-values (λ () (split-at lst n))
                        (λ (hd tl) (slice-up tl n (cons hd acc))))))

(define (mapcar f . xss)
  "A mufch better mapcar stolen from Muf."
  (define (aux acc . xss)
    (if (ormap empty? xss)
        (reverse acc)
        (apply aux (cons (apply f (map car xss)) acc) (map cdr xss))))
  (apply aux '() xss))

(define (transpose xss)
  "Just transpose pepega."
  (apply map list xss))

(define (zip . lists)
  "Huh i guess zipping is basically transposing"
  (apply mapcar list lists))

;; Tuples are assumed to be lists

(define (+. . tuples)
  (apply map + tuples))

(define (-. . tuples)
  (apply map - tuples))

(define (*. . tuples)
  (apply map * tuples))

(define (/. . tuples)
  (apply map / tuples))

(provide (all-defined-out) cut)
