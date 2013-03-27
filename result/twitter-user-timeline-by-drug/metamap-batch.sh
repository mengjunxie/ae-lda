#!/bin/bash

METAMAP_BIN=/Users/h0cked/dev/public_mm/bin/metamap11
METAMAP_OPTS="-L 2011 -Z 2011AB -V USAbase -A --XMLf --prune 35"

d=./R

if [ -d "$d" ]; then
    echo "processing files in $d..."


    if [ ! -d "$d/result" ]; then
        mkdir "$d/result"
    fi

    for f in ./$d/*.R.txt.processed.txt
    do
        b=$(basename $f)
        $METAMAP_BIN $METAMAP_OPTS $f "./$d/result/$b.xml"
        #echo $b
    done
fi