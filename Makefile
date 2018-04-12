# for minted, pygmentize is required: module load python/anaconda3

# the latex file are not included as make dependencies because latexmk
# is better at detecting dependency changes than make

front_matter:
	latexmk -pdf -xelatex -shell-escape abstract.tex
	latexmk -pdf -xelatex -shell-escape preface.tex
	latexmk -pdf -xelatex -shell-escape introduction.tex
	latexmk -pdf administrative_abstract.tex
	latexmk -pdf title_page.tex

dissertation:
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
