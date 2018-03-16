all:
	latexmk -pdf -xelatex -shell-escape presentation_outline.tex
	latexmk -pdf -xelatex -shell-escape presentation.tex

chemfig:
	latexmk -pdf -xelatex -shell-escape chemfig_examples.tex

faraday:
	latexmk -pdf faraday.tex

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
