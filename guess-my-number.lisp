;;;; guess-my-number.lisp
;;;; guess-my-number game using binary search
;;;; @author: Shyam Sreenivasan


(defparameter *small* 1
  " *small* is a global variable to store smallest range. ")

(defparameter *big* 100
   " *big* is a global variable to store biggest range. ")

(defun guess-my-number()
  " guess-my-number() guesses a number between the
range of *small* and *big*. ash function performs 
a arithmetic shift. "
  (ash (+ *small* *big*) -1))

(defun smaller()
  " smaller() lowers the *big* "
  (setf *big* (1- (guess-my-number)))
  (guess-my-number))

(defun bigger()
  " bigger() higher the *small* "
  (setf *small* (1- (guess-my-number)))
  (guess-my-number))

(defun start-over()
  " start-over() resets the lower and higher ranges to start
over. "
  (defparameter *small* 1)
  (defparameter *big* 100)
  (guess-my-number))
