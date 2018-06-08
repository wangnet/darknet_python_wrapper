# darknet python wrapper

Original: https://github.com/pjreddie/darknet

# Requirements

`cuda` `python3 opencv`

# Usage

Download yolov3 weights and clone darknet repository

`wget https://pjreddie.com/media/files/yolov3.weights`

`git clone https://github.com/pjreddie/darknet`

Make some change on darknet Makefile

`cd darknet`

`GPU=0` --> `GPU=1`

Compile darknet -> darknet, libdarknet.a, libdarknet.so

`make`

Copy shared library file, cfg, data and delete darknet source code (not necessary for darknet wrapper)

`cp libdarknet.so ../`
    
`cp -r cfg ../`

`cp -r data ../`

`cd ..`

`rm -rf darknet`

Run

`python3 darknet_video.py -i <source video path> -o <destination video path>`

press "q" to quit.

# Some useful variables in Makefile

`GPU=1` compile with cuda

`CUDNN=1` compile with cudnn

`OPENCV=1` compile with opencv (not necessary)

`DEBUG=1` compile in debug mode

`NVCC=nvcc` path to nvcc (usually /usr/local/cuda/bin/nvcc)


