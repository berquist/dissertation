all:
	latexmk -pdf -xelatex -shell-escape presentation.tex

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
