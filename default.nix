{ pkgs ? import <nixpkgs> { }, ... }:

pkgs.stdenv.mkDerivation {
  name = "eric-john-berquist-etd";
  src = ./.;
  buildInputs = with pkgs; [
    just
    python312Packages.pygments
    texliveFull
  ];
  buildPhase = ''
    just all
  '';
  installPhase = ''
    mkdir -p $out
    cp main.pdf $out
  '';
}
