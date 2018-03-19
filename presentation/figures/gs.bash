#!/bin/bash

inputs=(
    ../../diff_overlay.pdf
    application_of_ct.pdf
    frequencies_calc_vs_expt1_combined.pdf
)

for input in ${inputs[@]}; do
    stub=${input%.*}
    echo ${stub}
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=${stub}2.pdf ${stub}.pdf
done
# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=application_of_ct2.pdf application_of_ct.pdf
# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=frequencies_calc_vs_expt1_combined2.pdf frequencies_calc_vs_expt1_combined.pdf
