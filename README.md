# Most important things

[Tex.SE is your friend!](https://tex.stackexchange.com)

## Compilation

* Don't run a bunch of `pdflatex/bibtex` commands or use some crazy Makefile. `latexmk -pdf etd.tex` does _everything_. By crazy Makefile I mean that thing Adam uses for everything. Don't use it. See how my Makefile cleans some other files, but otherwise just calls `latexmk`.
* For `latexmk`, if you want to use `xetex/xelatex`, pass the `-xelatex` flag.
* If you're using `minted` to display source code, you must have the `pymgmentize` Python package installed and pass `-shell-escape` to `latexmk`.

* How to properly 'make' a latex project?: https://tex.stackexchange.com/q/40738/94717

# General

Answer to both: yes.

* Are `\(` and `\)` preferable to dollar signs for math mode?: https://tex.stackexchange.com/q/510/94717
* Why is `\[...\]` preferable to `$$...$$`?: https://tex.stackexchange.com/q/503/94717

For structure:

* When should I use `\input` vs. `\include`?: https://tex.stackexchange.com/q/246/94717

I and others use `\input` to avoid any page issues, and apparently it's much faster. For separate compilation, I used the `standalone` (rather than `subfiles`) package.

# Bibliography info

`pittetd` works just fine with `biblatex/biber`. See https://tex.stackexchange.com/q/25701/94717 for the differences between all the available options.

Dealing with messy libraries:

* https://tex.stackexchange.com/q/300962/94717
* https://tex.stackexchange.com/q/76420/94717

I mostly used JabRef, `sed`, and a text editor to do stuff by hand.

* JabRef will automatically convert bibtex -> biblatex, format many journal abbreviations, help with name formatting, ...
* `sed` to delete `abstract`, `keywords`, `mendeley-tags`; `sed -i '/mendeley-tags/d' library.bib`; this may cause compilation failure if fields are not on a single line but JabRef and trying to compile the document can point you to the line number that has junk, clean it by hand.

# `siunitx`

Used for proper typesetting of units and numbers, either combined or separately.

* Displaying plus/minus uncertainty: https://tex.stackexchange.com/q/27703/94717
* Also displaying plus/minus uncertainty: https://tex.stackexchange.com/q/234649/94717

This is specific to the `pittetd` class: you cannot put `\si`, `\SI`, or any other `siunitx` command in captions, because there will be complaints about undefined commands when making the list of figures/tables. The solution is to use a short caption (in `[]`) that doesn't contain `siunitx` commands. You will probably need to do this anyway so the captions don't go over a line on the lof/lot pages.

# How to do...?

* How to use `\graphicspath`: https://tex.stackexchange.com/a/139403/94717
* Scale an image to page width: https://tex.stackexchange.com/q/39147/94717
* Use of the `singlespace` environment: https://tex.stackexchange.com/a/49703/94717
* How to use conditionals: https://tex.stackexchange.com/q/61598/94717
* Conditionals defined by `standalone`: https://tex.stackexchange.com/a/356466/94717
* Subpreambles in `standalone`: https://tex.stackexchange.com/q/157274/94717

# Including source code

The best package to use is probably `minted`. [Here](https://tex.stackexchange.com/q/102596/94717) is a comparison of the most common options. `listings` is useful for plain text and looks good, but `minted` is probably what you're thinking of in terms of text editor syntax highlighting.

# Including Jupyter Notebooks

* Workflow for including jupyter (aka ipython) notebooks as pages in a LaTeX documents?: https://tex.stackexchange.com/q/289385/94717
