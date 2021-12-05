#!/bin/bash
increased=0
deacreased=0
count=0
while read line; do
    if [ ${count} -lt 1 ]; then
        x=${line}
    fi
    if [ ${count} -gt 0 ]; then
        y=${x}
        x=${line}
        if [ ${y} -lt ${x} ]; then
            ((increased+=1))
        elif [ ${y} -gt ${x} ]; then
            ((decreased+=1))
        fi
    fi
    ((count+=1))
done < puzzle1.txt

echo "$increased"
