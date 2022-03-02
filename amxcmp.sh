#!/bin/sh
DIR=/home/geetansh/test/amxcmp
AIRCONTROL_DIR=/home/geetansh/test/amxc/aircontrol
BSS_DIR=/home/geetansh/test/amxcmp/bss
ERROR_DIR=/home/geetansh/test/amxcmp/errot
for i in `ls $DIR`
do
    FILE=`echo ${i%%.*}`
    amxcmp -f $DIR/$i  -af  ${AIRCONTROL_DIR}/${FILE}_success.csv -bf ${BSS_DIR}/${FILE}_success.csv -e ${ERROR_DIR}/${FILE}_error.csv
done