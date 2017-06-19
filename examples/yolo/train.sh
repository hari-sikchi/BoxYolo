#!/usr/bin/env sh

CAFFE_HOME=../..

SOLVER=./gnet_solver.prototxt
WEIGHTS=/home/harshit/work/caffe-yolo/data/yolo/ZF.v2.caffemodel
#WEIGHTS=/home/harshit/work/caffe-yolo/models/bvlc_googlenet/bvlc_googlenet.caffemodel

$CAFFE_HOME/build/tools/caffe train \
    --solver=$SOLVER --weights=$WEIGHTS --gpu=0

