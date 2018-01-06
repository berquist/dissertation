#!/bin/sh

# pandoc -s -f markdown_github -t docx -o reviewer_comments_AbInitio.docx reviewer_comments_EJB_CAD.md
# pandoc -s -f markdown -t docx -o reviewer_comments_AbInitio.docx reviewer_comments_EJB_CAD.md
pandoc -s -f docx -t latex -o Spectroscopic_Map_revised.tex Spectroscopic_Map_revised.docx
