all:
	latexmk -pdf eric_john_berquist_etd.tex

clean:
	latexmk -c
	rm -f *.etd
