# for minted, pygmentize is required: module load python/anaconda3

all:
	latexmk -pdf -shell-escape eric_john_berquist_etd.tex

library: library.bib
	latexmk -pdf test_bibliography.tex

clean:
	latexmk -c
	rm -f *.etd
