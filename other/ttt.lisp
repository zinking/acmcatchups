(defun tictactoe ()
    "start playing tic tac toe game"
  (interactive)
  (switch-to-buffer "tictactoe")
  (ttt-mode)
  (ttt-init))

(defun ttt-init ()
  "start a new game of tic tac toe."
  (setq ttt-bd (make-vector (* bd-sz bd-sz) ?\.))
  (text-scale-increase 5)
  (ttt-print-bd)
  (setq ttt-player ?\X))

(defvar ttt-bd nil
  "the board itself")

(defconst bd-sz 3
  "the board size")

(define-derived-mode ttt-mode special-mode "tic tac toe"
    (define-key ttt-mode-map (kbd "C-;") 'ttt-mark))

(defun ttt-print-bd ()
  (let ((inhibit-read-only t))
    (erase-buffer)
    (dotimes (row bd-sz)
      (dotimes (col bd-sz)
        (insert (ttt-get-square  row col)))
      (insert "\n"))))


(defun ttt-get-square (row col)
  "get the cell of row col"
  (elt ttt-bd
       (+ col
          (* row
             bd-sz)))) 

(defun ttt-set-square (row col val)
  "set the cell of row col"
  (aset ttt-bd
       (+ col
          (* row
             bd-sz))
       val))

(defun ttt-mark ()
  "player make move"
  (interactive)
  (let ((row (- (line-number-at-pos) 1))
        (col (current-column)))
    (ttt-set-square row col ttt-player))
  (ttt-print-bd)
  (ttt-judge)
  (ttt-swap-players))


(defvar ttt-player nil
  "the character represent the player")

(defun ttt-swap-players ()
  "make it other player's turn"
  (setq ttt-player
        (if (char-equal ttt-player ?\X)
            ?\O
            ?\X))
  )

(defun ttt-judge ()
  "judge the game state"
  (when (ttt-game-won)
    (message "congrats! player %c won!" ttt-player))
  )

(defun ttt-game-won ()
  "return if player has won the game"
  (or (ttt-d-win)
      (ttt-r-win)
      (ttt-c-win)))

(defun ttt-d-win ()
  "wheter diagonal wins"
  (or (ttt-same-player
       (ttt-get-square 0 0)
       (ttt-get-square 1 1)
       (ttt-get-square 2 2))
      (ttt-same-player
       (ttt-get-square 0 2)
       (ttt-get-square 1 1)
       (ttt-get-square 2 0)
       )))


(defun ttt-c-win ()
  "whether column wins"
  (let ((has-won nil))
    (dotimes (col bd-sz)
      (when (ttt-same-player
             (ttt-get-square 0 col)
             (ttt-get-square 1 col)
             (ttt-get-square 2 col))
        (setq has-won t)))
    has-won))

(defun ttt-r-win ()
  "whether row wins"
  (let ((has-won nil))
    (dotimes (row bd-sz)
      (when (ttt-same-player
             (ttt-get-square row 0)
             (ttt-get-square row 1)
             (ttt-get-square row 2))
        (setq has-won t)))
    has-won)
  )

(defun ttt-same-player (s1 s2 s3)
  "determine whether the same player"
     (and (ttt-isplayer s1)
          (char-equal s1 s2)
          (char-equal s2 s3)))

(defun ttt-isplayer (sq)
  (or (char-equal sq ?\X)
      (char-equal sq ?\O)))
