(require 'org)

(defun oxodoo-create-project ()
  (interactive)
  (org-mode)
  (unless (save-excursion
    (goto-char (point-min))
    (search-forward "#+TITLE" nil))

  (insert (concat "#+TITLE: " (read-string " Odoo Project name:")))
  (insert "\n* Project \n")
  (insert "** Configuration \n")
  (insert "** Modules \n")

  ))

(defun oxodoo-create-model ()
  (interactive)
  (org-mode)


)

(defun oxodoo-create-module ()
  (interactive)
  (org-mode)
  (message "%s" (org-get-outline-path))
)

(defun insert-oxodoo ()
  (interactive)
  (insert "oxodoo"))

(define-minor-mode oxodoo-mode
  "Get your oxodoos in the right places."
  :lighter " oxodoo"
  :keymap (let ((map (make-sparse-keymap)))
            (define-key map (kbd "C-c p") 'oxodoo-create-project)
            (define-key map (kbd "C-c C-m") 'oxodoo-create-module)
            (define-key map (kbd "C-c C-d") 'oxodoo-create-model)
            map))
(provide 'oxodoo-mode)
