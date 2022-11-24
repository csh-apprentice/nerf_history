#!/bin/bash

echo Launching experiment $1
echo GPU $2
echo EXTRA ${@:3}

DEBUG_DIR=debug/$1
mkdir -p $DEBUG_DIR
NOHUP_FILE=$DEBUG_DIR/log
echo CKPT $DEBUG_DIR
echo LOGFILE $NOHUP_FILE

CUDA_VISIBLE_DEVICES=$2 nohup python -u debug.py -t $DEBUG_DIR ${@:3} > $NOHUP_FILE 2>&1 &
echo DETACH
