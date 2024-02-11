#!/bin/bash

if ! [ $# -eq 1 ]; then
    echo "USAGE:"
    echo "\t./format_tests.sh \"pasted_tests_string\""
    exit 1
fi

echo -n "$1" | tr '\n' ' ' | sed "s/keyboard_arrow_right//gi"
