#!/bin/bash

# gs.bash: Keynote outputs malformed PDF 1.3 files which LaTeX can't
# incorporate without visual glitches. Processing them with
# ghostscript first seems to fix any problems.

inputs=(
    ../../diff_overlay.pdf
    application_of_ct.pdf
    frequencies_calc_vs_expt1_combined.pdf
    psi4numpy_ecosystem2.pdf
)

for input in ${inputs[@]}; do
    stub=${input%.*}
    echo ${stub}
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=${stub}2.pdf ${stub}.pdf
done
