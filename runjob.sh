#!/bin/bash
ID=${1}
RA=${2}
DEC=${3}
python3 createcutout.py F125W.fits ${RA} ${DEC}
python3 createcutout.py F160W.fits ${RA} ${DEC}
python3 createcutout.py F814W.fits ${RA} ${DEC}
python3 createcolorimage.py ${ID}
