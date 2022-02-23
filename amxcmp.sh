#!/bin/sh
DIR=/home/geetansh/test/amxcmp
SUCCESS_DIR=/home/geetansh/test/amxcmp
ERROR_DIR=/home/geetansh/test/amxcmp
for i in `ls $DIR`
do
    FILE=`echo ${i%%.*}`
    amxcmp -f $DIR/$i  -o  ${SUCCESS_DIR}/${FILE}_success.csv -e ${ERROR_DIR}/${FILE}_error.csv
done