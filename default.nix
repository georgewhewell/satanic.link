 with import <nixpkgs> {}; {
   pyEnv = stdenv.mkDerivation {
     name = "py";
     buildInputs = [
      python35Packages.python
    ];
    shellHook = ''
      if [ ! -d env ]
      then
        python3 -m venv env
      fi
      source env/bin/activate
    '';
   };
 }
