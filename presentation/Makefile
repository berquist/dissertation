all:
	latexmk -pdf -xelatex -shell-escape presentation.tex

chemfig:
	latexmk -pdf -xelatex -shell-escape chemfig_examples.tex

faraday:
	latexmk -pdf faraday.tex

clean:
	latexmk -c
	rm -f *.bbl *.etd *.html *.lbf *.loa *.lol *.nav *.pyg *.run.xml *.snm *.stp *.vrb *.xdv
	rm -rf ./_minted*
