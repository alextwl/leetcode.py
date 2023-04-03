#!/bin/bash
#
# Launch default browser and open Leetcode problem webpage I've solved by number.
#

BASEURL="https://leetcode.com/problems/"

if [[ -z "$1" ]]; then
    echo "Usage: $0 <problem_number>"
    echo "e.g. $0 222"
    exit 0
fi

DIR=$(dirname "$0")/all
pushd ${DIR} > /dev/null 2>&1
PROBLEM=$(find . -regex '\./[0]*'"$1"'-.*\.py'|head -n 1)
popd > /dev/null 2>&1

if [[ -z "${PROBLEM}" ]]; then
    echo "problem not found."
    exit 1
fi

re='\./[0-9]*-(.*)\.py'
if [[ "$PROBLEM" =~ $re ]]; then
    PROBLEM_ID=${BASH_REMATCH[1]}
    $(which x-www-browser) "${BASEURL}${PROBLEM_ID}/" 1>/dev/null 2>/dev/null & disown
fi

