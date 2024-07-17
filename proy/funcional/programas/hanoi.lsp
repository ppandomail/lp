(defun torres-de-hanoi (discos)
    (interactive "nDime tus discos y te digo cuantos pasos tienes que dar: " discos)
    (message (number-to-string (torres-de-hanoi-aux discos))))
  (defun torres-de-hanoi-aux (discos)
    (if (= discos 1)
        1
      (+ 1 (* 2 (torres-de-hanoi-aux (- discos 1))))))