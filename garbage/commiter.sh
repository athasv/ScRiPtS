#!/bin/sh

ISSUE=$(git symbolic-ref HEAD 2> /dev/null | cut -b 14-)
MSG=$(awk -v msg="Refs #$ISSUE -" 'NR==1{print msg}{print $0}' $1)

echo "$MSG" > $1

ISSUE=$(git symbolic-ref HEAD 2> /dev/null | cut -b 14-)
COLS=$((${#ISSUE} + 10))
subl -n -w "$*:1:$COLS"

# Source:https://gist.github.com/m4dz/5030223
