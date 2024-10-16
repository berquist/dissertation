all: pdflatex xelatex chemrxiv
	latexmk -pdf psi4numpy.tex


pdflatex:
	latexmk -pdf pandoc.tex
	latexmk -pdf -shell-escape pandoc_minted.tex
	latexmk -pdf -shell-escape test_source_code.tex
	latexmk -pdf tutorial.tex

xelatex:
	latexmk -pdf -shell-escape -xelatex test_source_code_xelatex.tex
	# can't compile tutorial_redone.tex on its own
	latexmk -pdf -shell-escape -xelatex tutorial_redone_standalone.tex

chemrxiv:
	latexmk -pdf psi4numpy_chemrxiv_2.tex

clean:
	latexmk -C
