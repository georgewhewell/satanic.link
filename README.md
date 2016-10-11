# satanic.link

[![Build Status](https://travis-ci.org/georgewhewell/satanic.link.svg?branch=master)](https://travis-ci.org/georgewhewell/satanic.link)

Hosts the free satanic link shortening service at [satanic.link](satanic.link)

# development

clone this repository:

    git clone git@github.com:georgewhewell/satanic.link.git
    
with [nix](https://nixos.org/nix/) package manager installed, run:

    cd satanic-link && nix-shell 
    pip install -r requirements.txt

# running

run server with:

    python3 sataniclink/app.py
    
