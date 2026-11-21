#!/bin/sh
TARGET=marvin.local:/home/crackers/kobots/
DOIT="rsync -avz --progress --exclude __pycache__ --delete"
${DOIT} marvin.py ${TARGET}
${DOIT} edlib ${TARGET}
# async stuff
${DOIT} pybot ${TARGET}
${DOIT} m2_smooth.py ${TARGET}
# deps
${DOIT} pyproject.toml ${TARGET}

