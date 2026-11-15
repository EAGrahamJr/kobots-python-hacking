#!/bin/sh
TARGET=murphy.local:/home/crackers/kobots/
DOIT="rsync -avz --progress --exclude __pycache__ --delete"
${DOIT} murphy.py ${TARGET}
${DOIT} edlib ${TARGET}
# async stuff
${DOIT} pybot ${TARGET}
${DOIT} m2_smooth.py ${TARGET}

