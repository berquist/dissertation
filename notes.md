# Most important things

[Tex.SE is your friend!](https://tex.stackexchange.com)

## Compilation

* Don't run a bunch of `pdflatex/bibtex` commands or use some crazy Makefile. `latexmk -pdf etd.tex` does _everything_. By crazy Makefile I mean that thing Adam uses for everything. Don't use it. See how my Makefile cleans some other files, but otherwise just calls `latexmk`.
* For `latexmk`, if you want to use `xetex/xelatex`, pass the `-xelatex` flag.
* If you're using `minted` to display source code, you must have the `pymgmentize` Python package installed and pass `-shell-escape` to `latexmk`.

# Bibliography info

`pittetd` works just fine with `biblatex/biber`. See https://tex.stackexchange.com/q/25701/94717 for the differences between all the available options.

Dealing with messy libraries:

* https://tex.stackexchange.com/q/300962/94717
* https://tex.stackexchange.com/q/76420/94717

I mostly used JabRef, `sed`, and a text editor to do stuff by hand.

* JabRef will automatically convert bibtex -> biblatex, format many journal abbreviations, help with name formatting, ...
* `sed` to delete `abstract`, `keywords`, `mendeley-tags`; `sed -i '/mendeley-tags/d' library.bib`; this may cause compilation failure if fields are not on a single line but JabRef and trying to compile the document can point you to the line number that has junk, clean it by hand.

# How to do...?

* How to use `\graphicspath`: https://tex.stackexchange.com/a/139403/94717
* Use of the `singlespace` environment: https://tex.stackexchange.com/a/49703/94717
* How to use conditionals: https://tex.stackexchange.com/q/61598/94717
* Conditionals defined by `standalone`: https://tex.stackexchange.com/a/356466/94717
* Subpreambles in `standalone`: https://tex.stackexchange.com/q/157274/94717
