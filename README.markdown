# PhD dissertation

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>. Chapters 3 and 4 are copyright the American Chemical Society.

License text taken from [here](https://github.com/idleberg/Creative-Commons-Markdown/blob/15d16f11204c13dd8c226a0c189ad22dc8c84517/4.0/by-nc-sa.markdown). Badge taken from [here](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba). See [here](https://creativecommons.org/choose/#metadata) for how the metadata was generated.

## Installation

Either

    git clone --recurse-submodules https://github.com/berquist/dissertation.git

or

    git clone https://github.com/berquist/dissertation.git
    cd dissertation
    git submodule update --init

See [the HOWTO](HOWTO.markdown) for more information.

### Requirements

#### Python (`pip install <name>`)

    pygmentize

#### Ubuntu (`sudo apt-get install <name>`)

    texlive-science
    latexmk
    biber
    texlive-bibtex-extra
