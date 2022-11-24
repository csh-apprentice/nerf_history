#!/bin/bash

echo Launching experiment $1
echo CKPTDIR $2
echo DATADIR $3
echo SGDIR   $4

PRO_DIR=evaluate/$1
mkdir -p $PRO_DIR
LOG_FILE=$PRO_DIR/log
echo PRO_DIR $PRO_DIR
echo LOGFILE $LOG_FILE


#CUDA_VISIBLE_DEVICES=$2 nohup python -u choose_point.py -t $3 > $NOHUP_FILE 2>&1 &
nohup python -u evaluate.py $2 $4 $3 > $LOG_FILE 2>&1 &
