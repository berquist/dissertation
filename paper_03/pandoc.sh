#!/bin/sh

# pandoc -s -f docx -t latex -o Spectroscopic_Map_revised.tex Spectroscopic_Map_revised.docx
# pandoc -s -f docx -t latex -o Spectroscopic_Map_Final.tex Spectroscopic_Map_Final.docx
pandoc -s -f docx -t latex -o SI.tex SI.docx
