set -e # Stop if error

pdflatex --shell-escape main.tex
bibtex main
pdflatex --shell-escape main.tex
pdflatex --shell-escape main.tex
