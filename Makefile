# for minted, pygmentize is required: module load python/anaconda3

all:
	latexmk -pdf -shell-escape eric_john_berquist_etd.tex

clean:
	latexmk -c
	rm -f *.etd
