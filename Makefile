# for minted, pygmentize is required: module load python/anaconda3

all:
	latexmk -pdf -xelatex -shell-escape eric_john_berquist_etd.tex

library: library.bib
	latexmk -pdf -xelatex test_bibliography.tex

clean:
	latexmk -c
	rm -f *.bbl
	rm -f *.etd
	rm -f *.loa
	rm -f *.lol
	rm -f *.pyg
	rm -f *.run.xml
	rm -f *.stp
	rm -f *.xdv
	rm -rf ./_minted*
