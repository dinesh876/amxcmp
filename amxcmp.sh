#!/bin/sh
DIR=/home/geetansh/test/amxcmp
AIRCONTROL_DIR=/home/geetansh/test/amxc/aircontrol
BSS_DIR=/home/geetansh/test/amxcmp/bss
AIRCONTROL_ERROR_DIR=/home/geetansh/test/amxcmp/cmp_error
BSS_ERROR_DIR=/home/geetansh/test/amxcmp/bss_error
for i in `ls $DIR`
do
    FILE=`echo ${i%%.*}`
    amxcmp -f $DIR/$i  -af  ${AIRCONTROL_DIR}/${FILE}_success.csv -bf ${BSS_DIR}/${FILE}_success.csv -ce ${AIRCONTROL_ERROR_DIR}/${FILE}_aircontrol_error.csv -ef ${BSS_ERROR_DIR}/${FILE}_bss_error.csv
done