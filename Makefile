# for minted, pygmentize is required: module load python/anaconda3

# You want latexmk to *always* run, because make does not have all the
# info.  Also, include non-file targets in .PHONY so they are run
# regardless of any file of the given name existing.
.PHONY: eric_john_berquist_etd.pdf all clean

# The first rule in a Makefile is the one executed by default
# ("make"). It should always be the "all" rule, so that "make" and
# "make all" are identical.
all: eric_john_berquist_etd.pdf

# In case you didn't know, '$@' is a variable holding the name of the
# target, and '$<' is a variable holding the (first) dependency of a
# rule.

eric_john_berquist.pdf: eric_john_berquist.tex
	latexmk -pdf -xelatex -shell-escape eric_john_berquist_etd.tex

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

library: library.bib
	latexmk -pdf -xelatex test_bibliography.tex

