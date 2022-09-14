{ pkgs }: {
  deps = [
		pkgs.python38Packages.beautifulsoup4
		pkgs.python38Packages.pycryptodome
    pkgs.python38Packages.lxml
    pkgs.python38Packages.requests
    pkgs.python38Packages.pip
    pkgs.python38Full
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}