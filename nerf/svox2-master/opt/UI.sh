#!/bin/bash

echo Launching experiment $1
echo CKPTDIR $2
echo DATADIR $3

UI_DIR=UI/$1
mkdir -p $UI_DIR
LOG_FILE=$UI_DIR/log
echo UI_DIR $UI_DIR
echo LOGFILE $LOG_FILE


#CUDA_VISIBLE_DEVICES=$2 nohup python -u choose_point.py -t $3 > $NOHUP_FILE 2>&1 &
nohup python -u UI.py $2 $3 > $LOG_FILE 2>&1 &
