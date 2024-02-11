#!/bin/bash

if ! [ $# -eq 1 ]; then
    input="$(wl-paste)"
else
    input="$1"
fi

echo -n "$input" | sed "s/keyboard_arrow_right//gi" > format_tmp
sed "s/$/||/" format_tmp | tr -d '\n' | wl-copy

rm -f format_tmp
