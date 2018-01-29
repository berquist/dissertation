#!/bin/bash

# jupyter nbconvert --to latex 6b_first_hyperpolarizability.ipynb
# This is most useful for later pandoc consumption.
jupyter nbconvert --to markdown 6b_first_hyperpolarizability.ipynb
# jupyter nbconvert --to pdf 6b_first_hyperpolarizability.ipynb
# jupyter nbconvert --to python 6b_first_hyperpolarizability.ipynb

pandoc --listings -f markdown -t latex 6b_first_hyperpolarizability.md -s -o pandoc.tex

pandoc --filter ~/repositories/pandoc-minted_nick-ulle/pandoc-minted.py -f markdown -t latex 6b_first_hyperpolarizability.md -s -o pandoc_minted.tex
latexmk -pdf -shell-escape pandoc_minted.tex
