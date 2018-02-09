#!/bin/bash
set -evx

mkdir ~/.axecore

# safety check
if [ ! -f ~/.axecore/.axe.conf ]; then
  cp share/axe.conf.example ~/.axecore/axe.conf
fi
