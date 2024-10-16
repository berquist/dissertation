# for minted, pygmentize is required: module load python/anaconda3

# the latex file are not included as make dependencies because latexmk
# is better at detecting dependency changes than make

all: front_matter library
	$(MAKE) dissertation

dissertation:
	latexmk -pdf eric_john_berquist_etd.tex

# This is useful for making all the things Pitt requires for its
# administrative submission stuff.
front_matter:
	latexmk -pdf abstract.tex
	latexmk -pdf preface.tex
	latexmk -pdf introduction.tex
	latexmk -pdf administrative_abstract.tex
	latexmk -pdf title_page.tex

library: library.bib
	latexmk -pdf test_bibliography.tex

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
